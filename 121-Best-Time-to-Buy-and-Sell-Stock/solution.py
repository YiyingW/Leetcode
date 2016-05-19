class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_history = float("inf")
        max_result = 0
        for i in range(0, len(prices)):
            current = prices[i]
            min_stock = min(min_history, current)
            new = current - min_stock
            max_result = max(maxProfit(prices[0:i],new))
        
        return max_result
            
            
        