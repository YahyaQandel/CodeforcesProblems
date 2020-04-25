import unittest
from datastructure.src.Hashtable import HashTable


class HashTableTest(unittest.TestCase):

    def setUp(self):
        self.hashtable = HashTable()

    def testHashTablePutAndGet(self):
        self.hashtable.put("Yahya", 1100)
        self.hashtable.put("Adel", 5300)
        self.hashtable.put("hhh", 4000)

        self.assertEqual(self.hashtable.get("Adel"), 5300)
        self.assertEqual(self.hashtable.get("hhh"), 4000)
        self.assertEqual(self.hashtable.get("Yahya"), 1100)
