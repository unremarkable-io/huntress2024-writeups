#!/usr/bin/env python3
import base64
from pathlib import Path
from zipfile import ZipFile

with ZipFile((Path(__file__).parent.joinpath('base64by32.zip'))) as zf:
    with zf.open('base64by32') as f:
        data = f.read()
        while data := base64.b64decode(data):
            if b'flag{' in data:
                print(data.decode().strip())
                break
