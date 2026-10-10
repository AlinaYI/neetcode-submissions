class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                curr = prices[right] - prices[left]
                profit = max(profit, curr)
            else:
                left = right
            right += 1
        return profit