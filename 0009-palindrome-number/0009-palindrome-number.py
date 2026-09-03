class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        temp=str(x)
        reverse=temp[::-1]
        if temp==reverse:
            return True
        else:
            return False
               