#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

def hash_starts_with_5_zeros(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    hash = m.hexdigest()

    if hash[0:5] == '00000':
        return hash[5]

    return None

def get_next_character(id, number):
    """

    >>> from pprint import pprint
    >>> pprint(get_next_character('abc', 0))
    (3231929, '1')
    >>> pprint(get_next_character('abc', 3231930))
    (5017308, '8')
    """

    character = hash_starts_with_5_zeros('%s%i' % (id, number))
    while character == None:
        number += 1
        character = hash_starts_with_5_zeros('%s%i' % (id, number))

    return (number, character)

def get_passcode(id):
    """

    >>> print(get_passcode('abc'))
    18f47a30
    >>> print(get_passcode('ffykfhsq'))
    c6697b55
    """

    number = 0
    passcode = ''

    while len(passcode) < 8:
        (number, character) = get_next_character(id, number)
        passcode += character
        number += 1

    return passcode

def hash_starts_with_5_zeros_and_position(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    hash = m.hexdigest()

    if hash[0:5] == '00000':
        return hash[5:7]

    return None

valid_positions = ('0', '1', '2', '3', '4', '5', '6', '7')

def check_string_for_position(string):
    hash = hash_starts_with_5_zeros_and_position(string)
    if hash != None and hash[0] in valid_positions:
        return (int(hash[0]), hash[1])
    return None

def get_next_character_v2(id, number):
    """

    >>> from pprint import pprint
    >>> pprint(get_next_character_v2('abc', 0))
    (1, '5', 3231929)
    >>> pprint(get_next_character_v2('abc', 3231930))
    (4, 'e', 5357525)
    """

    result = check_string_for_position('%s%i' % (id, number))
    while result == None:
        number += 1
        result = check_string_for_position('%s%i' % (id, number))

    return (result[0], result[1], number)

def get_passcode_v2(id):
    """

    >>> print(get_passcode_v2('ffykfhsq'))
    ac35d825
    """

    number = 0
    passcode = ['_', '_', '_', '_', '_', '_', '_', '_']

    while '_' in passcode:
        (position, character, number) = get_next_character_v2(id, number)
        print(position, character, number)
        if passcode[position] == '_':
            passcode[position] = character
        number += 1

    return ''.join(passcode)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

