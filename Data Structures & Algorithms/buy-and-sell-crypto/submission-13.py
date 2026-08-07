class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        profit = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right]-prices[left] )
        return profit
            