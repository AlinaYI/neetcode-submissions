class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 答案具有单调性
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right-left)//2

            totalHour = 0
            for i in range(len(piles)):
                totalHour += math.ceil(piles[i]/mid)
            
            if totalHour > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
