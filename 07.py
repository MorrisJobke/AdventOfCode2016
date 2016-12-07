#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def check(string):
    """

    >>> print(check('abba'))
    True
    >>> print(check('abcd'))
    False
    >>> print(check('qwer'))
    False
    >>> print(check('ioxxoj'))
    True
    """

    result = re.search(r'(.)(.)\2\1', string)

    if result is None:
        return False

    if result.group(1) == result.group(2):
        return False

    return True

example = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""

def supports_tls(lines):
    """

    >>> print(supports_tls(example.split('\\n')))
    2
    >>> print(supports_tls(open('07-01.txt', 'r').read().split('\\n')))
    110
    """

    count = 0
    for line in lines:
        part3 = line
        found = False
        miss = False
        while '[' in part3:
            (part1, rest) = part3.split('[', 1)
            (part2, part3) = rest.split(']', 1)
            if check(part1):
                found = True
            if check(part2):
                miss = True
            if miss:
                break
        if miss:
            continue

        if check(part3):
            found = True

        if found:
            count +=1

    return count

if __name__ == "__main__":
    import doctest

    doctest.testmod()

