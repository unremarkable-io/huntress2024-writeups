# Hidden Streams

This was related to streams in SysMon (https://www.youtube.com/watch?v=rrAGRdxf154).

One-liner solve using `evtx_dump` and [Binary Refinery](https://github.com/binref/refinery):

```shell
% evtx_dump Sysmon.evtx | grep Contents | r.csd b64
flag{bfefb891183032f44fa93d0c7bd40da9}
```
