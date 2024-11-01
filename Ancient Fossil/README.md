# Ancient Fossil

```shell
% binwalk -qe ancient.fossil && grep -r flag _ancient.fossil.extracted/
```

or a one-liner solve with `sqlite3` and [Binary Refinery](https://github.com/binref/refinery):

```shell
% sqlite3 ancient.fossil 'select hex(content) from blob;' | r.resplit '\n' [| r.hex | r.snip 4: | r.zl | r.rex 'flag{.*}' ]
```

or install fossil in Kali, use this as a DB and click yourself to death in the GUI :-)
