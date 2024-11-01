#!/usr/bin/env python3

msg = '146 154 141 147 173 061 064 145 060 067 062 146 067 060 065 144 064 065 070 070 062 064 060 061 144 061 064 061 143 065 066 062 146 144 143 060 142 175'

for part in msg.split(' '):
    print(chr(int(part, 8)), end='', flush=True)
