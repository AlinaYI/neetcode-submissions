class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        这道题要做的就是看什么

        double for loop, find out each profit combinations
        maximum On2 O1

        two pointers, since sell from feature
        right 一直往右扫；left 只在发现更低价格时更新。
        '''

        profit = 0

        left = right = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                profit = max(profit, curr_profit)
            else:
                left = right

            right += 1                  
        
        return profit
 