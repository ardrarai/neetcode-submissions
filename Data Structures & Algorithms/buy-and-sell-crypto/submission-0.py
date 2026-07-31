class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # buy and sell
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r  # because we want to update to the lowest possible value and here that would be value of r
            r = r+1
        return maxProfit