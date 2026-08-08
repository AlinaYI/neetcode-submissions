class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        # 这里要求的就是最小的speed
        # max = max(piles)
        # 最小的speed就是从1开始

        # sum( piles[i]/speed for i in range(len(pikes))) < 9

        left = 1
        right = max(piles)

        while left <= right:
            
            mid = left + (right-left)//2

            need_hour = 0
            for i in range(len(piles)):
                need_hour += math.ceil(piles[i]/mid)

            if need_hour <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
