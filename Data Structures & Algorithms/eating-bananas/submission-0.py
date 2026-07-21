class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        totol = speed x hour
        '''

        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right - left)//2

            hour_need = 0
            for i in range(len(piles)):
                hour_need += math.ceil(piles[i]/mid)

            if hour_need > h:
                left = mid + 1
            else:
                right = mid - 1

        return left