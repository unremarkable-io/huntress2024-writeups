# Echo Chamber

One-liner solve with [Binary Refinery](https://github.com/binref/refinery):

```shell
% tshark -r echo_chamber.pcap -Y 'icmp.type == 8' -T fields -e data.data | r.resplit [ | r.snip :2 ] | r.hex | r.rex 'flag{.*}'
```

More manual approach implemented in [`echo_chamber.py`](echo_chamber.py).
