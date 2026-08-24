class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # value, idx
        q = deque()
        res = []
        for idx, value in enumerate(nums):
            
            if q and idx - q[0][1] + 1 > k:
                q.popleft()

            while q and q[-1][0] < value:
                q.pop()
            q.append( (value, idx) )

            if idx >= k-1:
                res.append(q[0][0])
        return res