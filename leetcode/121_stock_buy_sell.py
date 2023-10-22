# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        initial_purchase_price = prices[0]
        profit = -10000
        for price_index in range(1, len(prices)):
            if prices[price_index] < initial_purchase_price:
                initial_purchase_price = prices[price_index]
            elif prices[price_index] - initial_purchase_price > profit:
                profit = prices[price_index] - initial_purchase_price

        if profit < 0:
            return 0
        return profit


if __name__ == "__main__":
    solution = Solution()
    solution.maxProfit([7, 6, 4, 3, 1])
