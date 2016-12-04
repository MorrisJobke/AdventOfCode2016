#!/usr/bin/env python
# -*- coding: utf-8 -*-


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def walk(position, direction, instruction):
    d = instruction[0]
    steps = int(instruction[1:])

    if d == 'R':
        direction = (direction + 1) % 4
    elif d == 'L':
        direction = (direction + 4 - 1) % 4

    if direction == NORTH:
        position = (position[0], position[1] + steps)
    elif direction == EAST:
        position = (position[0] + steps, position[1])
    elif direction == SOUTH:
        position = (position[0], position[1] - steps)
    elif direction == WEST:
        position = (position[0] - steps, position[1])

    return (position, direction)

def get_distance(instructions):
    """

    >>> from pprint import pprint
    >>> pprint(get_distance('R2, L3'))
    5
    >>> pprint(get_distance('R2, R2, R2'))
    2
    >>> pprint(get_distance('R5, L5, R5, R3'))
    12
    >>> pprint(get_distance('R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1'))
    271
    """

    position = (0, 0)
    direction = NORTH

    for instruction in instructions.split(', '):
        (position, direction) = walk(position, direction, instruction)

    return abs(position[0]) + abs(position[1])

def first_location_visited_twice(instructions):
    """

    >>> from pprint import pprint
    >>> pprint(first_location_visited_twice('R8, R4, R4, R8'))
    4
    >>> pprint(first_location_visited_twice('R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1'))
    153
    """

    position = (0, 0)
    direction = NORTH
    visited = []
    i_was_here = False

    for instruction in instructions.split(', '):
        d = instruction[0]
        steps = int(instruction[1:])
        for i in range(steps):
            if position in visited:
                # I already was here - leave it
                i_was_here = True
                break

            visited.append(position)
            (position, direction) = walk(position, direction, '%s%i' % (d, 1))
            d = '_' # make no turn hack by setting the turn direction to _ instead of L/R ;)
        if i_was_here:
            break

    return abs(position[0]) + abs(position[1])

if __name__ == "__main__":
    import doctest

    doctest.testmod()

