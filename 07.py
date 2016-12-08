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


def clean(string):
    """

    >>> print(clean("dqpthtgufgzjojuvzvm[eejdhpcqyiydwod]iingwezvcbtowwzc[uzlxaqenhgsebqskn]wcucfmnlarrvdceuxqc[dkwcsxeitcobaylhbvc]klxammurpqgmpsxsr"))
    dqpthtgufgzjojuvzvm[]iingwezvcbtowwzc[]wcucfmnlarrvdceuxqc[]klxammurpqgmpsxsr
    """

    return re.sub(r'\[[^\]]*\]', r'[]', string)

def clean_inverse(string):
    """

    >>> print(clean_inverse("dqpthtgufgzjojuvzvm[eejdhpcqyiydwod]iingwezvcbtowwzc[uzlxaqenhgsebqskn]wcucfmnlarrvdceuxqc[dkwcsxeitcobaylhbvc]klxammurpqgmpsxsr"))
    [eejdhpcqyiydwod][uzlxaqenhgsebqskn][dkwcsxeitcobaylhbvc]
    """

    string = re.sub(r'\][^\[]+\[', r'][', string)
    string = re.sub(r'^[^\[]+\[', r'[', string)

    return re.sub(r'\][^\[]+$', r']', string)

def find_groups(string):
    """

    >>> print(find_groups("dqpthtgufgzjojuvzvm[eejdhpcqyiydwod]iingwezvcbtowwzc[uzlxaqenhgsebqskn]wcucfmnlarrvdceuxqc[dkwcsxeitcobaylhbvc]klxammurpqgmpsxsr"))
    ['hth', 'ojo', 'zvz', 'ucu', 'xsx']
    >>> print(find_groups("zazbz"))
    ['aza', 'bzb']
    """

    cleaned = clean(string)

    a = []
    for i in range(0, len(cleaned) - 2):
        result = re.findall(r'((.)(.)\2)', cleaned)

        for r in result:
            if r[1] != r[2]:
                # invert group
                tmp = r[2] + r[1] + r[2]
                if tmp not in a:
                    a.append(tmp)

        cleaned = cleaned[1:]

    return a

def contains_group(string, groups):
    cleaned = clean_inverse(string)

    for group in groups:
        if group in cleaned:
            return True

    return False


example2 = """
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb"""

def support_ssl(lines):
    """

    >>> print(support_ssl(example2.split('\\n')))
    3
    >>> print(support_ssl(open('07-01.txt', 'r').read().split('\\n')))
    242
    """

    count = 0

    for line in lines:
        groups = find_groups(line)
        if contains_group(line, groups):
            count += 1
            continue

    return count

if __name__ == "__main__":
    import doctest

    doctest.testmod()
