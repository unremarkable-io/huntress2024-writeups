#!/usr/bin/env python3
from io import BytesIO
from pathlib import Path


def xor(x: bytes, y: bytes) -> bytes:
    return bytes([a ^ b for a, b in zip(x, y)])


# sub_7FF66C3E72D0((size_t *)Buf1, (const void *)(rc_data_ptr + 248), 580uLL, rc_data_ptr + 1076, 580LL);
with open(Path(__file__).parent / 'rusty_bin', 'rb') as f:
    f.seek(0x478E08)  # offset of first part (also at offset 248 of 'RCDATA/100/1033')
    data1 = f.read(580)
    f.seek(0x479144)  # offset of second part (also at offset 1076 of 'RCDATA/100/1033')
    data2 = f.read(580)

data = BytesIO(xor(data1, data2))

assert data.read(4) == b'HNTR'

chunks_nr = int.from_bytes(data.read(4), 'big')  # no idea why this is big endian
chunks = {}
for _ in range(2):  # each chunk_id is present twice, those two pieces have to be XORed to get plaintext
    for _ in range(chunks_nr):
        chunk_id = int.from_bytes(data.read(4), 'little')
        offset = int.from_bytes(data.read(4), 'little')
        length = int.from_bytes(data.read(4), 'little')
        pos = data.tell()
        data.seek(offset)
        if chunk_id not in chunks:
            chunks[chunk_id] = data.read(length)
        else:
            chunks[chunk_id] = xor(chunks[chunk_id], data.read(length)).decode()
        data.seek(pos)

# DEBUG
# for chunk_id, chunk in sorted(chunks.items()):
#     print(chunk_id, chunk)

for chunk_id in range(10):
    print(chunks[chunk_id], end='', flush=True)
print()
