# GoCrackMe1

Trivial RE - random string XORed with a single byte key:

```c
qmemcpy(v17, "0:71-44coc``3dg0cc3c`nf2cno0e24435f0n+", sizeof(v17));
for ( i = 0LL; i < 38; ++i )
  v2[i] = v17[i] ^ 'V';
```

Decode as:

```shell
% r.emit '0:71-44coc``3dg0cc3c`nf2cno0e24435f0n+' | r.xor 'V'
flag{bb59566e21f55e5680d589f3dbbec0f8}
```