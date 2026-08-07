class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 求speed
        # totalnumber/speed == hours
        # sum(piles[i]/speed) <= h
        # 最大：max(piles)
        # 最小：1
        
        def TotalHour(speed):
            hour = 0
            for i in range(len(piles)):
                hour += math.ceil(piles[i]/speed)
            return hour

        left = 1
        right = max(piles)

        while left <= right:

            mid = left + (right-left)//2

            if TotalHour(mid) <= h:
                right = mid-1
            else:
                left = mid + 1
        return left