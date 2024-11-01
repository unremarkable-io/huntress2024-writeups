#!/usr/bin/env python3
from io import BytesIO
from pathlib import Path

from PIL import Image
from pyzbar import pyzbar
from pyzbar.pyzbar import Decoded

decoded_data: Decoded = pyzbar.decode(Image.open(Path(__file__).parent.joinpath('qrcode.png')))[0]
qr2_bytes = decoded_data.data.decode('unicode_escape').encode('latin1')  # get stupid bytes as string to actual bytes
print(pyzbar.decode(Image.open(BytesIO(qr2_bytes)))[0].data.decode())
