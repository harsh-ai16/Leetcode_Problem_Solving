class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)
        def upperbound():
            ub=n
            high=n-1
            low=0
            while low<=high:
                mid=(high+low)//2
                if nums[mid]>target:
                    ub=mid
                    high=mid-1
                else:
                    low=mid+1
            return ub
            
        def lowerbound():
            lb=-1
            high=n-1
            low=0
            while low<=high:
                
                mid=(high+low)//2
                if nums[mid]>=target:
                    lb=mid
                    high=mid-1
                else:
                    low=mid+1
            return lb
        lb=lowerbound()
        ub=upperbound()

        if lb==-1 or nums[lb]!=target:
            return [-1,-1]
        else:
            return[lb,ub-1]
            
        