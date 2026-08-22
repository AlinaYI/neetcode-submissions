class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # value, idx
        q = deque()
        res = []
        for i in range(len(nums)):
            if q and i - q[0][1] + 1 > k:
                q.popleft()

            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))

            if i >= k-1:
                res.append(q[0][0])
        return res