class Solution:
    def peakIndexInMountainArray(self, nums):
        s ,e = 0,len(nums)-1
        while(s<=e):
            mid = int(s+(e-s)/2)
            if nums[mid-1] < nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid+1]:
                e = mid
            else:
                s = mid + 1
        return e
