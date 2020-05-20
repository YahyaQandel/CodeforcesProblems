import unittest
from datastructure.src.BMHeap import BMHeap


class BMHeapTest(unittest.TestCase):

    def setUp(self):
        self.BMHeap = BMHeap()

    def testInsert(self):
        self.BMHeap.insert(42)
        self.BMHeap.insert(29)
        self.BMHeap.insert(18)
        self.BMHeap.insert(35)

        self.BMHeap.__str__()
