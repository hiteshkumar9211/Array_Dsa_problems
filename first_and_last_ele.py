class Solution:
    def firstOccurence(self,nums,target):
        s = 0
        e = len(nums)-1
        mid = s + (e-s)//2
        ans = -1
        while(s<=e):
            if self.nums[mid] == self.target:
                ans = mid
                e = mid - 1
            elif self.nums[mid]>self.target:
                e = mid - 1
            else:
                s = mid + 1
            mid = s + (e-s)//2
        return ans
    def lastOccurence(self,nums,target):
        s = 0
        e = len(nums)-1
        mid = s + (e-s)//2
        ans = -1
        while(s<=e):
            if self.nums[mid] == self.target:
                ans = mid
                s = mid + 1
            elif self.nums[mid]>self.target:
                e = mid - 1
            else:
                s = mid + 1
            mid = s + (e-s)//2
        return ans

    def searchRange(self, nums, target):
        self.pair_ans = []
        self.pair_ans.append(self.firstOccurence(self,nums,target))
        self.pair_ans.append(self.lastOccurence(self,nums,target))
        return self.pair_ans
