class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #这里就是要找到一个speed
        # piles[i]/speed + < h

        # maxSpeed = max([piles])
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right-left)//2

            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid)
            
            if total > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left