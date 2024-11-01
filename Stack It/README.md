# Stack It

```shell
% r.emit '53515155525E560701040D020003565B0F50070153500B505500515B01065306' | r.hex | r.xor 1ecff8bece9486287dc76521a84bb7c0
b4234f4bba4685dc84d6ee9a48e9c106
```

I also wrote [`stack_it.py`](stack_it.py) that uses angr and symbolic execution to print memory at the right time.

Or this (Thanks [@alphillips-lab](https://github.com/alphillips-lab)):
```shell
% r.emit stack_it.bin | r.vstack 0x8049000
```
