# GoCrackMe3

There are several places in the binary where an error like "Access Denied!" is printed and it exits. One needs to patch
all of this out (I just swapped the conditions from e.g. `jz` to `jnz` or `nop`-ed it out if code flow allowed).

Get to the point that it prints:

> ...but I can tell you that the flag is 38 characters long.

Find that string in memory during execution (debugging), around the same address the flag can be found as well (that 
is how I first-blooded the challenge).

Alternatively the binary can be patched so that one of the print statements is pointed to the flag buffer itself.
`bsdiff`/`bspatch` patch is in "GoCrackMe3.patch" if you are interested:

```shell
% bspatch GoCrackMe3 GoCrackMe3.patched GoCrackMe3.patch
```

```shell
$ ./GoCrackMe3.patched
flag{42024a30b221fccaa8edda76fdc232b2}
...but I can tell you that the flag is 38 characters long.
```
