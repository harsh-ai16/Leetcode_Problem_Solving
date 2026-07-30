class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        maxs=nums[0]
        count=0
        for i in range(n):
            count+=nums[i]
            if count>maxs:
                maxs=count
            if count<0:
                count=0
        return maxs
        