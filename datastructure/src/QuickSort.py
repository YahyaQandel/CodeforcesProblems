class QuickSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        def __quicksort(arr):
            if len(arr) == 0 or len(arr) == 1:
                return arr
            pivot = arr[0]
            less_than_pivot_arr = []
            greater_than_pivot_arr = []
            # less_than_pivot_arr = [i for i in arr[1:] if i < pivot]
            # greater_than_pivot_arr = [i for i in arr[1:] if i > pivot]
            for i in arr:
                if i < pivot:
                    less_than_pivot_arr.append(i)
                elif i > pivot:
                    greater_than_pivot_arr.append(i)
            return (
                __quicksort(less_than_pivot_arr)
                + [pivot]
                + __quicksort(greater_than_pivot_arr)
            )

        return __quicksort(self.data)
