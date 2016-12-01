#!/usr/bin/env python

"""
First day problem.
pfh 12/1/16
"""

import logging

MOVES = "L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1"


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(funcName)s] %(message)s')
log = logging.getLogger('day1')


class DayOne():

    def __init__(self):
        self.compass = ['N', 'E', 'S', 'W']
        self.addmap = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Initial state
        self.orientation = 0 # index into compass array
        self.coordinates = {'x': 0, 'y': 0}


    def __repr__(self):
        return '(' + str(self.coordinates['x']) + ',' + str(self.coordinates['y']) + ') facing ' + self.compass[self.orientation] + ' distance ' + str(self.distance())


    def _turn(self, direction):
        if direction == 'R':
            self.orientation = ((self.orientation + 1) % len(self.compass))
        else:
            if self.orientation > 0:
                self.orientation -= 1
            else:
                self.orientation = 3


    def move(self, move):
        # eg R2
        rel_direction = move[0]
        distance = int(move[1:])
        log.debug('Move ' + rel_direction + ' dist ' + str(distance))

        log.debug('before ' + str(self))

        self._turn(rel_direction)

        self.coordinates['x'] += (self.addmap[self.orientation][0] * distance)
        self.coordinates['y'] += (self.addmap[self.orientation][1] * distance)

        log.debug('after ' + str(self))

    def distance(self):
        return abs(self.coordinates['x']) + abs(self.coordinates['y'])


    def multimove(self, moves_string):
        move_array = moves_string.split(', ')
        for move in move_array:
            self.move(move)


if __name__ == '__main__':
    d1 = DayOne()
    d1.multimove(MOVES)
    log.info(d1)