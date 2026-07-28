class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        d={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in d:
                return [d[remaining],i]
            d[nums[i]]=i
        