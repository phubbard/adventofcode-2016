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

    self.compass = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.data = MOVES.split(', ')
        self.orientation = 0 # index into compass array
        self.coordinates = {'x': 0, 'y': 0}

        log.debug('Initialized ' + str(len(self.data)) + ' moves')


    def _turn(self, direction):
        if direction == 'R':
            self.orientation = ((self.orientation + 1) % len(self.compass))
        else:
            if self.orientation > 0:
                self.orientation -= 1;
            else:
                self.orientation = 3;


    def move(self, move):
        # eg R2
        rel_direction = move[0]
        distance = move[1]

        self._turn(rel_direction)



    def distance(self):
        return self.coordinates['x'] + self.coordinates['y']


    def multimove(self, moves_string):
        pass
