# Revenge of Discount Programming Devices

## Garbage quick solve (see below for nicer one)

```shell
% # see the snip of the first character here - there was some garbage there - NEED TO PAY ATTENTION TO STUFF LIKE THAT! was stuck on that for a bit
% r.emit ./challenge | r.xtpyi challenge.pyc | r.rev | r.carve b64 -s | r.snip 1: | r.b64 | r.zl | r.loop 49 'rev:csd[b64]:zl' > 2.py
% # edit 2.py and uncomment the lines - only does print() should be safe to run
% python3 2.py > 3.py
% # 3.py looks safe to run too - only does print and unzip
% python3 3.py | r.loop 50 'rev:csd[b64]:zl'
```

## Proper one-line solve

One-liner solve with [Binary Refinery](https://github.com/binref/refinery):

```shell
% r.ef ./challenge | r.xtpyi challenge.pyc | r.rev | r.carve b64 -s | r.snip 1: | r.b64 | r.zl | r.loop 49 'rev:csd[b64]:zl' | r.carve intarray | r.pack | r.carve string -n10 -d [| r.pop key [| r.xor var:key ]] | r.loop 50 'rev:csd[b64]:zl'
```
