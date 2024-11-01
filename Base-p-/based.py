#!/usr/bin/env python3
import base64
import gzip
from io import BytesIO
from pathlib import Path

import base65536
from PIL import Image

data = open(Path(__file__).parent.joinpath('based.txt'), 'r').read().strip()  # and get rid of newline at the end
decoded = gzip.decompress(base64.b64decode(base65536.decode(data)))  # decode all the bases/gzips/whatever
# open('based.png', 'wb').write(decoded) # just for debugging

# parse the image programmatically
image = Image.open(BytesIO(decoded))
output = bytearray()
for x in range(87, 1300, 100):  # iterate over all the squares in X-axis
    output.extend(image.getpixel((x, 100)))  # Y-axis is constant

print(output.decode())
