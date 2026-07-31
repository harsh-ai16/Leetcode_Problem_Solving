class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        nl=[0]*n
        j=0
        k=1
        for i in nums:
            if i>0:
                nl[j]=i
                j+=2
            else:
                nl[k]=i
                k+=2

        return nl
        