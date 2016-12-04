#!/usr/bin/env python
# -*- coding: utf-8 -*-

example = """541  588  421
  827  272  126
  660  514  367
   39  703  839
  229  871    3
  237  956  841
  898  566  112
  101   79  112
  813  541  146
  603  135  565
  335  363  180
  382  493  669"""

def valid_triangle(side_lengths):
    """

    >>> from pprint import pprint
    >>> pprint(valid_triangle(' 5 10 25'))
    False
    >>> pprint(valid_triangle('5 10 12'))
    True
    """
    tmp_sides = side_lengths.strip()
    while '  ' in tmp_sides:
        tmp_sides = tmp_sides.replace('  ', ' ')
    sides = tmp_sides.split(' ')

    if len(sides) != 3:
        raise Exception('invalid: ', sides, tmp_sides, side_lengths)

    a = int(sides[0])
    b = int(sides[1])
    c = int(sides[2])
    if a + b <= c:
        #print('side c too short')
        return False
    if a + c <= b:
        #print('side b too short')
        return False
    if b + c <= a:
        #print('side a too short')
        return False

    return True

def count_valid_triangles(triangles):
    """

    >>> from pprint import pprint
    >>> pprint(count_valid_triangles(example.split('\\n')))
    7
    >>> pprint(count_valid_triangles(open('03-01.txt', 'r').read().split('\\n')))
    993
    """

    count = 0
    for triangle in triangles:
        if triangle.strip() == '':
            continue
        if valid_triangle(triangle):
            count += 1

    return count



def count_valid_triangles_vertically(triangles):
    """

    >>> from pprint import pprint
    >>> pprint(count_valid_triangles_vertically(example.split('\\n')))
    12
    >>> pprint(count_valid_triangles_vertically(open('03-01.txt', 'r').read().split('\\n')))
    1849
    """

    groups = []

    count = 0
    for line in triangles:
        groups.append(line)
        if len(groups) == 3:
            if valid_triangle('%s %s %s' % (groups[0].split()[0],groups[1].split()[0],groups[2].split()[0])):
                count += 1
            if valid_triangle('%s %s %s' % (groups[0].split()[1],groups[1].split()[1],groups[2].split()[1])):
                count += 1
            if valid_triangle('%s %s %s' % (groups[0].split()[2],groups[1].split()[2],groups[2].split()[2])):
                count += 1
            groups = []


    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()

