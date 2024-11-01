#!/usr/bin/env python3
import hashlib

data = 'squiqhyiiycfbudeduutvehrhkjki'

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

deroted = rot_alpha(10)('squiqhyiiycfbudeduutvehrhkjki')
print(f'rot10: {deroted}')
print(f'flag{{{hashlib.md5(deroted.encode()).hexdigest()}}}')
