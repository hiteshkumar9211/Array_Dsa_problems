class Solution:
    def __init__(self):
        self.arr = arr
    def largest(self,n,arr):
        n = len(arr)
        largest = arr[0]
        #early exit.
        if len(arr) == 1:
            return largest
        elif len(arr)!=1:
            for i in range(len(arr)):
                if arr[i]>largest:
                    largest = arr[i]
            return largest
