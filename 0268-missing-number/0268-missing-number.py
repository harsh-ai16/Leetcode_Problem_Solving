class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=(n*(n+1))//2
        c=0
        for i in nums:
            c+=i

        missing_number=(s-c)
        return missing_number
        