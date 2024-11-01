#!/usr/bin/env python3
from dataclasses import dataclass
from itertools import cycle
from pathlib import Path

from crccheck.crc import Crc32Base


@dataclass
class PngChunk:
    length: int
    name: str
    data: bytes
    crc: int

    def __post_init__(self):
        if Crc32Base.calc(self.name.encode() + self.data) != self.crc:
            raise ValueError(f'CRC mismatch on chunk "{self.name}"')


class PngFile:
    def __init__(self, filename: str):
        self.filename = filename
        self.chunks = []
        with open(self.filename, 'rb') as f:
            if f.read(8) != b'\x89PNG\r\n\x1a\n':
                raise ValueError('Unexpected PNG header')
            while chunk_len := int.from_bytes(f.read(4), 'big'):
                self.chunks.append(
                    PngChunk(chunk_len, f.read(4).decode(), f.read(chunk_len), int.from_bytes(f.read(4), 'big'))
                )


def parse_png_proper(filename: str):
    """
    This actually properly parses a PNG file format unlike the two craps above.
    """
    print(f'----- {filename} -----')
    png_file = PngFile(Path(__file__).parent.joinpath(filename).as_posix())

    decrypted = bytearray()
    for chunk in sorted(filter(lambda x: x.name.startswith('biT'), png_file.chunks), key=lambda x: x.name):
        for data_byte, xor_key_byte in zip(chunk.data, cycle(chunk.name.encode())):
            decrypted.append(data_byte ^ xor_key_byte)
    decrypted_string = decrypted.rstrip(b'\xAA').decode()  # remove padding from the end and decode to string
    print(decrypted_string)


def main():
    parse_png_proper('inconspicuous.png')


if __name__ == '__main__':
    main()
