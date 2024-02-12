class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = len(prices)

        max_profit = 0
        # if s < 2:
        #     return max_profit

        min_price = prices[0]

        for i in range(1, s):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)

        return max_profit