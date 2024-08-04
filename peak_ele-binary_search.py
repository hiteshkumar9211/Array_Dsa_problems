class Solution:
    def peakElement(self, arr, n):
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            # Base cases (similar to recursive approach)
            if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
                return mid

            # Move towards the increasing side
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return -1  # If no peak is found (unlikely with valid input)
