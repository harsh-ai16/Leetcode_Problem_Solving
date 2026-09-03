class Solution(object):
    def isPalindrome(self, x):
        temp=x
        original=temp
        n=len(str(temp))
        result=0
        if temp<0:
            return False
        for i in range(n):
            a=temp%10
            result=result*10+a
            temp=temp//10
        return original==result        