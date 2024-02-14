class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=len(prices)
        max_profit = 0

        for i in range(1, s):
            # Calculate profit by selling on the same day (if it's positive)
            profit_on_same_day = prices[i] - prices[i - 1]
            if profit_on_same_day > 0:
                max_profit += profit_on_same_day

        return max_profit