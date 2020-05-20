class BubbleSort:
    data = [5, 4, 3, 2, 1]

    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1 - i):
                if self.data[j] > self.data[j + 1]:
                    self.swap(j, j + 1)

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp
