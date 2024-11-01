import logging

import pwn


logging.basicConfig(level=logging.INFO)


def main():
    r = pwn.remote('challenge.ctf.games', 30075)
    while True:
        try:
            if data := r.recvuntil(b'Opponent move: ', timeout=30):
                logging.debug('DEBUG: %s', data)
                if data is None or data == b'':
                    print('timeout')
                    break
            opponent = r.recvline().strip()
            print('opponent', opponent)
            match opponent:
                case b'retreat':
                    print('our move: strike')
                    r.sendline(b'strike')
                case b'strike':
                    r.sendline(b'block')
                    print('our move: block')
                case b'advance':
                    r.sendline(b'retreat')
                    print('our move: retreat')
                case b'block':
                    print('our move: strike')
                    r.sendline(b'advance')
                case _:
                    print('WADAFAK NO IDEA')
        except EOFError:
            print('Got EOFError, breaking out of the loop')
            break

    # r.interactive is probably easier/better
    r.interactive()

    # for _ in range(5):
    #     print('recvrepeat', r.recvrepeat(5))


if __name__ == '__main__':
    main()
