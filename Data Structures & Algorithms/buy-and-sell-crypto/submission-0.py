class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        max_profit = 0

        while l < r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1

        return max_profit

        