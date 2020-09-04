class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_value = float('inf')

    def push(self, x: int) -> None:
        temp = []
        if not self.data:
            temp.append(x)
            temp.append(x)
            self.data.append(temp)
            return
        current_min = self.data[0][1]
        self.data.insert(0, [x, min(x, current_min)])

    def pop(self) -> None:
        self.data.remove(self.data[0])

    def top(self) -> int:
        if self.data:
            return self.data[0][0]
        else:
            return None

    def getMin(self) -> int:
        if self.data:
            return self.data[0][1]
        else:
            return None
