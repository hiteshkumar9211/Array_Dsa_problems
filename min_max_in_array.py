class Solution:
    def __init__(self):
        self.arr = arr
    def get_min_max(self, arr):
        min = arr[0]
        max = arr[0]
        for j in range(len(arr)):
            if arr[j]<min:
                min = arr[j]
        for i in range(len(arr)):
            if arr[i]>max:
                max = arr[i]
        return (min,max)
