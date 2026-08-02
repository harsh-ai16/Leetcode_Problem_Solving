class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)
        c=0
        e=set(nums)
        if n==0:
            return 0
        else:
            for i in e:
                l=1
                d=i
                if d-1 not in e:
                    while d+1 in e:
                        l+=1
                        d+=1
                    c=max(c,l)
            return (c)
        