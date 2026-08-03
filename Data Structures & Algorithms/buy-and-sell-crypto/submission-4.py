class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        这道题要做的就是看哪天的profit最大
        '''

        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                temp = prices[j] - prices[i]
                profit = max(profit, temp)
        return profit