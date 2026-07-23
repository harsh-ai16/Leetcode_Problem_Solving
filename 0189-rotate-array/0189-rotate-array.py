class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k%=n
        def func(nums,l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1

        func(nums,n-k,n-1)
        func(nums,0,n-k-1)
        func(nums,0,n-1)

        