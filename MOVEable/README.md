# MOVEable

This challenge is .. full of traps :)

This piece of code that is obvious SQL injection:

```python
conn = get_db()
c = conn.cursor()
sql = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
c.executescript(sql)
user = c.fetchone()
if user:
    ...
```

Is actually a BIG rabbithole, `c.executescript(sql)` can execute stacked queries but it has no output to the cursor,
no matter what. I was stuck here for a while until I realized that. Then I used stacked queries to:

1. insert my own session into `activesessions`
2. insert my own file into `files`

The file I inserted into files was a pickle RCE payload that got triggered on a request
to `/download/<filename>/<sessionid>`, however, the remote machine has no access to internet, so remote shell is not
really possible.

Back to exfiltrating data in a different way - I ended up making an `eval()` that called `flash()`, which printed data
into the warning box on the website.

After that I realized the app is running as `uid=1000(moveable)`, flag is nowhere to be seen, but `sudo -l` shows that
the user `uid=1000(moveable)` can run anything using sudo.

Ended up finding flag in `/root/flag.txt`.

See [`moveable.py`](moveable.py) for an automated solution.
