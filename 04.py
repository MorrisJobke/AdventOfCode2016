#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_checksum(id):

    counts = {}
    max = 0

    for char in id:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

        if counts[char] > max:
            max = counts[char]

    checksum = ''
    for i in range(max, 0, -1):
        chars = []
        for char, count in counts.items():
            if count == i:
                chars.append(char)

        chars.sort()

        checksum += ''.join(chars)

        if len(checksum) >= 5:
            break

    return checksum[0:5]

def split_it(room):
    (id, sector_and_checksum) = room.rsplit('-', 1)
    (sector, checksum) = sector_and_checksum.split('[')
    checksum = checksum[:-1]

    return (id, int(sector), checksum)


def is_real_room(room):
    """

    >>> from pprint import pprint
    >>> pprint(is_real_room('aaaaa-bbb-z-y-x-123[abxyz]'))
    123
    >>> pprint(is_real_room('a-b-c-d-e-f-g-h-987[abcde]'))
    987
    >>> pprint(is_real_room('not-a-real-room-404[oarel]'))
    404
    >>> pprint(is_real_room('totally-real-room-200[decoy]'))
    0
    """

    (id, sector, checksum) = split_it(room)
    id = id.replace('-', '')

    to_be = get_checksum(id)
    if to_be == checksum:
        return sector

    return 0

def check_them(rooms):
    """

    >>> check_them(open('04-01.txt', 'r').read().split('\\n'))
    ('northpole-object-storage', 324)
    245102
    """
    sum = 0

    for room in rooms:
        result = is_real_room(room)
        sum += result
        if result > 0:
            real_name = get_real_name(room)
            if 'north' in real_name[0]:
                print(real_name)

    print(sum)


def rotate(letter, number):
    """

    >>> print(rotate('a', 26))
    a
    >>> print(rotate('a', 13))
    n
    """

    number = number % 26

    ord_letter = ord(letter) + number

    if ord_letter > ord('z'):
        ord_letter -= 26

    return chr(ord_letter)

def get_real_name(room):

    (id, sector, checksum) = split_it(room)

    decrypted = ''
    for c in id:
        if c == '-':
            decrypted += '-'
            continue
        decrypted += rotate(c, sector)

    return (decrypted, sector)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

