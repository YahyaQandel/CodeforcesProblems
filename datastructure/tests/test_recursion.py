import unittest
from datastructure.src.RecursionExample import RecursionExample


class RecursionTest(unittest.TestCase):
    def testStripTextZeros(self):
        self.rcx = RecursionExample()
        self.assertEqual("1", self.rcx.strip_zeros("0001"));
        self.assertEqual("11", self.rcx.strip_zeros("0011"));
        self.assertEqual("1989", self.rcx.strip_zeros("00001989"));
        self.assertEqual("VOD", self.rcx.strip_zeros("VOD"));
