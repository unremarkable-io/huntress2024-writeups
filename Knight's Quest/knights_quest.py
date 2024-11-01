#!/usr/bin/env python3

input_data = b'BODUAhkDMLj3ZM7cfo9UBlt1ANUBY7LnecdpghL8mgZYJs6bhonfMQzeDjspI4LQ'


def orig_ida_decode(data: bytes) -> str:
    output = bytearray()
    for i in range(32):
        var1 = ((data[i + 32] ^ data[i]) & 0xff) % 0x3E
        var2 = var1 + ord('A')
        print(f'var1={var1} ({chr(var1)}), var2={var2} ({chr(var2)})')
        result = var1 + ord('A')
        if var1 + ord('A') > ord('Z'):
            if var2 >= ord('a'):
                if var2 > ord('z'):
                    result = var1 - 10
            else:
                result = var1 + 71

        output.append(result)
    return output.decode()


decoded = orig_ida_decode(input_data)
print('result:', decoded)
assert decoded == 'hmafgAhAalqmQABBOAZtP3OWFegsQDAB'

"""
Got this out of the game through debugging (later)

Your flag submission password is: hmafgAhAalqmQABBOAZtP3OWFegsQDAB
Press enter to exit the game...
"""
