# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Two pointers: "buy" and "sell".
# Sell pointer should always point to the later
# time period than the buy pointer.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr, sell_ptr = 0, 1
        max_profit = 0

        while sell_ptr < len(prices):
            profit = prices[sell_ptr] - prices[buy_ptr]

            if profit > 0: # sell price is larger than buy
                max_profit = max(max_profit, profit)
            else:
                # sell price is lower than buy ->
                # -> it is potentially new optimal "buy" point
                buy_ptr = sell_ptr

            sell_ptr += 1

        return max_profit
