# Knight's Quest

## Couple ways

### 1. Static RE

See [`knights_quest.py`](knights_quest.py).

### 2. Debugging
Put a breakpoint at `0x498CEE test    rdx, rdx`, set `RDX` to 0 (zero) and continue - it will jump out of a loop that
makes you fight monsters and print flag

### 3. Patching

Find the `Gorthmog, Destroyer Of Worlds` string, XREF to its init near `0x498AD0` and patch the `mov`
instructions at `0x498AFB` to set its life to something you can beat. (Thanks [@alphillips-lab](https://github.com/alphillips-lab))

## Submit to server

```shell
% curl -X POST -H "Content-Type: application/json" -d '{"password":"hmafgAhAalqmQABBOAZtP3OWFegsQDAB"}' http://challenge.ctf.games:31192/submit
{"flag":"flag{40b5b7e5395ee921cbbc804d4350b9c1}"}
```