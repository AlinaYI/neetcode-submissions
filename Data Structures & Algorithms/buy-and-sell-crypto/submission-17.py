class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # On
        # O1
        res = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    res = max(res, prices[j] - prices[i])
        return res
        '''

        left = 0
        res = 0
        for right in range(len(prices)):
            if prices[right] > prices[left]:
                res = max(res, prices[right]-prices[left])
            else:
                left = right
        
        return res