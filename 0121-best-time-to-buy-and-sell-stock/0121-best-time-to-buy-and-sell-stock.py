class Solution(object):
    def maxProfit(self, prices):
       n=len(prices)
       maxprofit=0
       minvalue=float("inf")
       for i in range(0,n):

        minvalue=min(minvalue,prices[i])
        maxprofit=max(maxprofit,prices[i]-minvalue)
       return maxprofit
    
        