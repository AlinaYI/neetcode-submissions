class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        这里就是把两个最大的石头拿出来，然后比大小
        所以也就是要一个maxHeap
        如果不相等，就把abs(stone1-stone2)放入stones
        '''

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            if stone1 != stone2:
                heapq.heappush(stones, stone1-stone2)
        
        stones.append(0)
        return abs(stones[0])