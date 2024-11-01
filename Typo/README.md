# Typo

```shell
ssh -p 31709 user@challenge.ctf.games # Password is "userpass"
```

- after login `sl` is run (locomotive) and then it exits
- you can just do `ssh -p 31709 user@challenge.ctf.games bash` to get non-interactive bash session
- then `cat flag.txt`
