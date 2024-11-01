# Strange Calc

The binary is upx packed (`upx -d calc.exe`). It drops `<randomstring>.jse` file in the same directory that is later
executed with `wscript.exe`.

The script utilized "JScript.Encode" non-sense encoding, use the function inside the javascript to decrypt the string to
get a flag.

Also, doable just using (Thanks [@alphillips-lab](https://github.com/alphillips-lab), who knew binary refinery has so
many features!):

```shell
% r.emit calc.exe | r.a3x | r.carve b64 -ds | r.wshenc | r.ppjscript
```