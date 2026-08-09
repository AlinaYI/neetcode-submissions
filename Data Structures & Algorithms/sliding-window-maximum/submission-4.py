class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # 如果right - idx < k-1说明超过了
        # 然后q里面放纸币前面大的数字，因为要keep maxi

        q = deque() # num, idx
        res = []
        # inital window
        for i in range(k):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append( (nums[i], i) )
        res.append(q[0][0])

        for right in range(k, len(nums)):

            while q and q[-1][0] < nums[right]:
                q.pop()
            q.append((nums[right], right))

            if right - q[0][1] + 1 > k:
                q.popleft()
            res.append(q[0][0])
        return res