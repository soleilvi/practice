'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

By Soleil Vivero
09/07/23
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        maxProfit = 0

        
        for price in prices:
            if price > max:
                max = price

            if price < min:
                min = price
                max = price
            
            if max - min > maxProfit:
                maxProfit = max - min
        
        return maxProfit
