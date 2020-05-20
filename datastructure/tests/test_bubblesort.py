import unittest
from datastructure.src.BubbleSort import BubbleSort


class BubbleSortTest(unittest.TestCase):

    def testSort(self):
        self.bubble_sort_obj = BubbleSort(data=[5, 4, 3, 2, 1])
        self.bubble_sort_obj.sort()
        self.assertEqual(self.bubble_sort_obj.data, [1, 2, 3, 4, 5])
        self.bubble_sort_obj = BubbleSort(data=[10, 2, 5, 30, 9])
        self.bubble_sort_obj.sort()
        self.assertEqual(self.bubble_sort_obj.data, [2, 5, 9, 10, 30])
