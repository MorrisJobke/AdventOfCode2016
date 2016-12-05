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

if __name__ == "__main__":
    import doctest

    doctest.testmod()

