class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        total = time x speed
        want speed
        '''

        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right-left)//2

            need_hour = 0
            for i in range(len(piles)):
                need_hour += math.ceil(piles[i]/mid)
            
            # hour 大，说明速度要加快
            if need_hour > h :
                left = mid + 1
            else:
                right = mid - 1

        return left