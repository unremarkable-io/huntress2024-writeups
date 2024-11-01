#!/usr/bin/env python3

def xor(x: bytes, y: bytes) -> bytes:
    return bytes([a ^ b for a, b in zip(x, y)])


res1 = xor(open('challenge-files/id_rsa_webserver', 'rb').read(), open('encrypted-files/id_rsa_webserver', 'rb').read())
print(res1.hex())
