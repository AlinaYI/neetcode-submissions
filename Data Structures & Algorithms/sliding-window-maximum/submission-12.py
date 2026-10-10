class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [2,1,4,6]
        # (num, idx)
        res = []
        q = deque()
        for idx, num in enumerate(nums):

            if q and idx-q[0][1]+1 > k:
                q.popleft()

            while q and q[-1][0] < num:
                q.pop()
            q.append( (num,idx) )

            if idx >= k-1:
                res.append(q[0][0])
        return res
