import unittest
from datastructure.src.QuickSort import QuickSort


class QuickSortTest(unittest.TestCase):
    def testSort(self):
        self.quicksort_obj = QuickSort(data=[5, 4, 3, 2, 1])
        self.quicksort_obj.sort()
        self.assertEqual(self.quicksort_obj.sort(), [1, 2, 3, 4, 5])
        self.quicksort_obj = QuickSort(data=[10, 2, 5, 30, 9])
        self.quicksort_obj.sort()
        self.assertEqual(self.quicksort_obj.sort(), [2, 5, 9, 10, 30])
