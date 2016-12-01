#!/usr/bin/env python

"""
Unit tests for day one, simply because TDD works.
pfh 12/1/16
"""


import unittest
import random
from day_one import DayOne


class TestDayOne(unittest.TestCase):

    def setUp(self):
        self.d1 = DayOne()

    def tearDown(self):
        pass

    def test_data(self):
        pass

    def test_one(self):
        moves = "R2, L3"
        self.d1.multimove(moves)
        self.assertEqual(self.d1.distance(), 5)

    def test_two(self):
        moves = "R2, R2, R2"
        self.d1.multimove(moves)
        self.assertEqual(self.d1.distance(), 2)

    def test_three(self):
        moves = "R5, L5, R5, R3"
        self.d1.multimove(moves)
        self.assertEqual(self.d1.distance(), 12)
