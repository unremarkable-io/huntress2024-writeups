# OceanLocust

This was solved by a hybrid approach of reverse engineering the rust binary and dynamically analyzing PNGs.

The process appends chunks to the PNG format with a name of `biT<byte>` which defines the order of these chunks
and serves as a xor key to demangle the data inside the chunk. The length of the data can vary and is defined
by an 4-byte value preceding the name (big-endian encoded).

See the complete solution in [`ocean_locust.py`](ocean_locust.py).
