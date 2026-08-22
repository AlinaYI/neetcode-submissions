class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def valid(speed):
            temp = 0
            for i in range(len(piles)):
                temp += math.ceil(piles[i]/speed)
            return temp <= h
        
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right-left)//2

            if valid(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
