class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque() # 存(num + idx)
        res = []
        for i in range(k):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
        res.append(q[0][0])

        for right in range(k, len(nums)):

            while q and q[-1][0] < nums[right]:
                q.pop()
            
            if q and right - q[0][1] > k - 1:
                q.popleft()
            
            q.append((nums[right], right))
            res.append(q[0][0])
        return res