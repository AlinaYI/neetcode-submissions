class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monostack ->  [2,4,6] 
        # 如果遇到了 num > stack[-1]: 加入q
        # 但是同时要maintain一个valid nums
        # 就是如果 currIdx - numIdx +1 > k, 超过范围，left remove
        # 可以用deque
        # deque : (num, idx)

        q = deque()
        res = []
        # initial first window
        for i in range(k):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append( (nums[i], i) )
        res.append(q[0][0])

        # [(2, 1)]

        for right in range(k, len(nums)):
            while q and q[-1][0] < nums[right]:
                q.pop()
            q.append( (nums[right], right) )
            
            while right - q[0][1] +1 > k:
                q.popleft()

            res.append(q[0][0])
        return res