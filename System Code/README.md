# System Code
 
First we found the `config.js` file from the website had additional content compared to original GitHub repository:

```
backupGlyphsTwr: ["a", "b", "c", "d", "e", "f"], // The characters to fallback to if glyphs fail to load
```

This and the hint about brute-forcing being allowed lead us to try brute-forcing 6 character long strings as a password.
It ended up being `bfdaec`.
