class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(0, len(prices)-1):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > maxprofit:
                    maxprofit = prices[j] - prices[i]
        return maxprofit