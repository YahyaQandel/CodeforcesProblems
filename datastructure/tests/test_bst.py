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

        self.assertEqual(self.bst.min().value, 1900)

    def testDeleteNoChildren(self):
        self.bst.insert(6, 6234)
        self.bst.insert(10, 1100)
        self.bst.insert(7, 7300)

        # Case 1 :- no children
        self.bst.delete(7)
        self.assertEqual(None, self.bst.get(7))

    def testDeleteOneChild(self):
        self.bst.insert(6, 6234)
        self.bst.insert(10, 1100)
        self.bst.insert(7, 7300)

        # Case 1 :- no children
        self.bst.delete(10)
        self.assertEqual(self.bst.get(6), 6234)
        self.assertEqual(None, self.bst.get(10))

    def testDeleteTwoChildren(self):
        self.bst.insert(7, 7300)
        self.bst.insert(10, 1100)
        self.bst.insert(6, 6234)

        # Case 1 :- no children
        self.bst.delete(7)
        self.assertEqual(self.bst.get(7), None)
        self.assertEqual(6234, self.bst.get(6))
        self.assertEqual(1100, self.bst.get(10))

    def testInOrderTraversal(self):
        self.bst.insert(10, "b")
        self.bst.insert(7, "c")
        self.bst.insert(6, "a")
        self.bst.insert(8, "k")
        self.bst.insert(12, "d")
        self.bst.insert(11, "e")
        self.bst.insert(13, "f")

        self.bst.in_order_traversal()

    def testPreOrderTraversal(self):
        self.bst.insert(10, "b")
        self.bst.insert(7, "c")
        self.bst.insert(6, "a")
        self.bst.insert(8, "k")
        self.bst.insert(12, "d")
        self.bst.insert(11, "e")
        self.bst.insert(13, "f")

        self.bst.pre_order_traversal()

    def testPostOrderTraversal(self):
        self.bst.insert(10, "b")
        self.bst.insert(7, "c")
        self.bst.insert(6, "a")
        self.bst.insert(8, "k")
        self.bst.insert(12, "d")
        self.bst.insert(11, "e")
        self.bst.insert(13, "f")

        self.bst.post_order_traversal()
