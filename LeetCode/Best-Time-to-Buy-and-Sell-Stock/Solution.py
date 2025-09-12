class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m=prices[0]
        r=0
        for i in range(1,len(prices)):
            m=min(m,prices[i])
            r=max(r,prices[i]-m)
        return r
        
        
        