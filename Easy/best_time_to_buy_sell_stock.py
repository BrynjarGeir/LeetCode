from typing import List, inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minPrice = 0, inf
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit