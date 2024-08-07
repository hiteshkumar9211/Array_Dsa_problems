class Solution:
    def peakIndexInMountainArray(self, nums):
        n = len(nums)-1
        s ,e = 0,n-1
        if(len(nums)==1):
            return 0
        if(nums[0]>nums[1]):
            return 0
        if(nums[n-1]>nums[n-2]):
            return n-1
        for i in range(n):
            if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                return i
       
