#!/usr/bin/env python3

import email
from pathlib import Path


def decode_multipart_related(data):
    msg = email.message_from_bytes(data)

    if msg.is_multipart():
        for i, part in enumerate(msg.walk()):
            # Check if the part is related to the main message
            if part.get_content_maintype() == 'multipart':
                continue

            # Access the content of the part
            payload = part.get_payload(decode=True)

            # Do something with the payload, e.g., print it
            open(f'file_{i}', 'wb').write(payload)


def main():
    decode_multipart_related(open(Path(__file__).parent.joinpath('ran_somewhere.eml'), 'rb').read())


if __name__ == '__main__':
    main()
