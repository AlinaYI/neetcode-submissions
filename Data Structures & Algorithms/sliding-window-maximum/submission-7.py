class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # non decreasing stack
        # also want to pop from front
        # chose deque
        # store value, idx
        q = deque()
        res = []
        
        for i in range(len(nums)):

            while q and i - q[0] +1 > k:
                q.popleft()

            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res