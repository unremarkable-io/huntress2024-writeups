#!/usr/bin/env python3

import re

# % tshark -r echo_chamber.pcap -Y 'icmp.type == 8' -T fields -e data.data > tmp

out = bytearray()
with open('tmp', 'r') as tmpfile:
    for line in tmpfile.readlines():
        out.append(bytes.fromhex(line.strip())[0])

if matches := re.findall(rb'flag\{[^}]+}', out):
    print('re.findall matches:', matches)

# flag is also present in an image like this
with open('image.png', 'wb') as outfile:
    outfile.write(out)
