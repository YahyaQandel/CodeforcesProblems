import unittest
from algorithms.src.Linkedlist import LinkedList


class LinkedInTest(unittest.TestCase):

    def setUp(self):
        self.linkedlist = LinkedList()

    def testAddBack(self):
        self.assertEqual(self.linkedlist.size(), 0)
        self.linkedlist.add_back(10)
        self.assertEqual(self.linkedlist.size(), 1)
        self.linkedlist.add_back(20)
        self.assertEqual(self.linkedlist.size(), 2)

    def testAddFront(self):
        self.assertEqual(self.linkedlist.size(), 0)
        self.linkedlist.add_front(10)
        self.assertEqual(self.linkedlist.size(), 1)
        self.linkedlist.add_front(20)
        self.assertEqual(self.linkedlist.size(), 2)

    def testGetFirst(self):
        self.linkedlist.add_back(10)
        self.linkedlist.add_back(20)
        self.linkedlist.add_back(30)
        self.assertEqual(self.linkedlist.get_first(), 10)

    def testGetLast(self):
        self.linkedlist.add_back(10)
        self.linkedlist.add_back(20)
        self.linkedlist.add_back(30)
        self.assertEqual(self.linkedlist.get_last(), 30)

    def testDeleteValue(self):
        self.assertEqual(self.linkedlist.size(), 0)
        self.linkedlist.add_back(10)
        self.linkedlist.add_back(20)
        self.linkedlist.add_back(30)

        self.linkedlist.delete(30)
        self.assertEqual(self.linkedlist.get_last(), 20)
        self.linkedlist.delete(10)
        self.assertEqual(self.linkedlist.get_first(), 20)

    def testSize(self):
        self.assertEqual(self.linkedlist.size(), 0)
        self.linkedlist.add_back(30)
        self.linkedlist.add_back(40)
        self.assertEqual(self.linkedlist.size(), 2)
        self.linkedlist.add_front(10)
        self.linkedlist.add_front(20)
        self.assertEqual(self.linkedlist.size(), 4)

    def testReverse(self):
        self.linkedlist.add_back(1)
        self.linkedlist.add_back(2)
        self.linkedlist.add_back(3)
        self.linkedlist.add_back(4)
        self.linkedlist.add_back(5)
        # print(self.linkedlist)
        self.linkedlist.reverse()
        print(self.linkedlist)
        self.assertEqual(self.linkedlist.get_first(), 5)

    def testReverseEdgeCaseWithOneElement(self):
        self.linkedlist.add_back(1)
        # print(self.linkedlist)
        self.linkedlist.reverse()
        print(self.linkedlist)
        self.assertEqual(self.linkedlist.get_first(), 1)

    def testMergeTwoLists(self):
        self.linkedlist.add_back(1)
        self.linkedlist.add_back(2)
        self.linkedlist.add_back(3)

        self.linkedlist2 = LinkedList()
        self.linkedlist2.add_back(4)
        self.linkedlist2.add_back(5)
        self.linkedlist2.add_back(6)
        self.linkedlist.merge_list(self.linkedlist2)
        self.assertEqual(self.linkedlist.get_first(), 1)
        self.assertEqual(self.linkedlist.get_last(), 6)

    def testSort(self):
        self.linkedlist.add_back(6)
        self.linkedlist.add_back(3)
        self.linkedlist.add_back(5)
        self.linkedlist.add_back(10)
        self.linkedlist.add_back(2)
        self.linkedlist.sort()
        self.assertEqual(self.linkedlist.get_first(), 2)
        self.assertEqual(self.linkedlist.get_last(), 10)

    def testPalindrome(self):
        self.linkedlist.add_back(1)
        self.linkedlist.add_back(2)
        self.linkedlist.add_back(3)
        self.linkedlist.add_back(2)
        self.linkedlist.add_back(1)
        self.assertTrue(self.linkedlist.is_palindrome())



def tearDown(self):
    self.linkedlist = None
