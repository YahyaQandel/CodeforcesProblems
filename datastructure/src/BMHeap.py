class BMHeap:

    def __init__(self):
        self.data = []
        self.size = 0

    def heapifyUp(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) < self.data[index]:
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)

    def insert(self, value):
        self.data.append(value)
        self.size += 1

        self.heapifyUp()

    def __str__(self):
        print(self.data)

    def left_child_index(self, index):
        return int(2 * index + 1)

    def right_child_index(self, index):
        return int(2 * index + 2)

    def parent_index(self, index):
        return int((index - 1) / 2)

    def has_parent(self, index):
        return self.parent_index(index) >= 0

    def has_left_child(self, index):
        return self.left_child_index(index) <= self.size

    def has_right_child(self, index):
        return self.right_child_index(index) <= self.size

    def left_child(self, index):
        return self.data[self.left_child_index(index)]

    def right_child(self, index):
        return self.data[self.right_child_index(index)]

    def parent(self, index):
        return self.data[self.parent_index(index)]

    def swap(self, index_one, index_two):
        temp = self.data[index_one]
        self.data[index_one] = self.data[index_two]
        self.data[index_two] = temp
