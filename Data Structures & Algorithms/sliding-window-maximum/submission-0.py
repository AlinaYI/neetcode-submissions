class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque() # 存 (value, index)，value 单调递减
        res = []
        for i in range(k):
            while q and nums[i] >= q[-1][0]:
                q.pop()
            q.append((nums[i], i))
        res.append(q[0][0])
        
        for right in range(k, len(nums)):

            while q and q[0][1] <= right - k:
                q.popleft()
            
            while q and nums[right] >= q[-1][0]:
                q.pop()
            
            q.append((nums[right], right))
            res.append(q[0][0])
        return res