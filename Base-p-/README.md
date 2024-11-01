# Base-p-

Almost a one-liner solve with [Binary Refinery](https://github.com/binref/refinery):

```shell
% r.emit based.txt | r.b65536 | r.b64 | r.zl | r.dump out.png
```

The resulting `out.png` has some colorful squares, the flag is encoded in the color hex codes. See [`based.py`](based.py) for an automated solution.
