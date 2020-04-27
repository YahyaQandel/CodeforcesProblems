import unittest
from datastructure.src.bst import Bst


class BSTTest(unittest.TestCase):

    def setUp(self):
        self.bst = Bst()

    def testGetAndInsert(self):
        self.bst.insert(10, 1100)
        self.bst.insert(7, 7300)
        self.bst.insert(1, 1900)
        self.bst.insert(4, 4600)
        self.bst.insert(8, 893)
        self.bst.insert(6, 6234)

        self.assertEqual(self.bst.get(3), None)
        self.assertEqual(self.bst.get(6), 6234)
        self.assertEqual(self.bst.get(7), 7300)
        self.assertEqual(self.bst.get(1), 1900)
        self.assertEqual(self.bst.get(4), 4600)
        self.assertEqual(self.bst.get(8), 893)

    def testGetMin(self):
        self.bst.insert(6, 6234)
        self.bst.insert(10, 1100)
        self.bst.insert(7, 7300)
        self.bst.insert(1, 1900)
        self.bst.insert(4, 4600)
        self.bst.insert(8, 893)

        self.assertEqual(self.bst.min(), 1900)
