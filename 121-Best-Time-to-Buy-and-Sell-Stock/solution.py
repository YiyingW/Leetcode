class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        min_stock = float("inf")
        max_result = 0
        for current in self.prices:
            min_stock = min(min_stock, current)
            new = current - min_stock
            max_result = max(max_result,new)
        return max_result

       

            
            
        