class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        nl=[]
        positive=[]
        negative=[]
        for i in range(0,n):
            if nums[i]>0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(0,n//2):
            nl.append(positive[i])
            nl.append(negative[i])
        return nl

        