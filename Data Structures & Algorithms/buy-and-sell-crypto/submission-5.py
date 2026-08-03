class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        这道题要做的就是看哪天的profit最大
        '''

        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         temp = prices[j] - prices[i]
        #         profit = max(profit, temp)
        # return profit

        left, right = 0,1
        profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                temp = prices[right] - prices[left]
                profit = max(profit, temp)
            else:
                left = right
            
            right += 1
        return profit
         

