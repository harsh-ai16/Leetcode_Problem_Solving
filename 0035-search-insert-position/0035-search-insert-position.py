class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        high=n-1
        low=0
        lb=n
        while low<=high:
            mid=(high+low)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
        