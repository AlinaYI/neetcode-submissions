class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # non decreasing stack
        # also want to pop from front
        # chose deque
        # store value, idx
        q = deque()
        res = []
        for i in range(k):
            while q and nums[i] > q[-1][0]:
                q.pop()
            q.append( (nums[i], i) )
        res.append(q[0][0])

        for right in range(k, len(nums)):
            while q and nums[right] > q[-1][0]:
                q.pop()
            q.append( (nums[right], right) )

            if right - q[0][1] + 1 > k:
                q.popleft()
            res.append(q[0][0])
        return res