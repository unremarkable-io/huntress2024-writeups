#!/usr/bin/env python3

one = bytes.fromhex('15b279d8c0fdbd7d4a8eea255876a0fd189f4fafd4f4124dafae47cb20a447308e3f77995d3c')
two = bytes.fromhex('73de18bfbb99db4f7cbed3156d40959e7aac7d96b29071759c9b70fb18947000be5d41ab6c41')

out = bytearray()
for a, b in zip(one, two):
    out.append(a ^ b)

print(out.decode())
