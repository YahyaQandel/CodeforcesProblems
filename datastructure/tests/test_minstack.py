import unittest
from datastructure.src.MinStack import MinStack


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack()

    def testPush(self):
        self.min_stack.push(10)
        self.min_stack.push(20)
        self.min_stack.push(30)
        self.assertEqual(self.min_stack.data[0][0], 30)

    def testPop(self):
        self.min_stack.push(10)
        self.min_stack.push(20)
        self.min_stack.push(30)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.data[0][0], 20)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.data[0][0], 10)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.data, [])

    def testTop(self):
        self.min_stack.push(10)
        self.min_stack.push(20)
        self.min_stack.push(30)
        self.assertEqual(self.min_stack.top(), 30)

    def testGetMin(self):
        self.min_stack.push(-2)
        self.min_stack.push(0)
        self.min_stack.push(-3)
        print(self.min_stack.data)
        self.assertEqual(self.min_stack.getMin(), -3)
        self.min_stack.pop()
        print(self.min_stack.data)
        self.assertEqual(self.min_stack.getMin(), -2)
        self.min_stack.push(-45)
        self.assertEqual(self.min_stack.getMin(), -45)
