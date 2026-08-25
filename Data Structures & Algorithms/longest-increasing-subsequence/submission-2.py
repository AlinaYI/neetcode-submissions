from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        这里需要make 的decision就是选择当前的数字加入之前还是新开一个increased subsequence
            []
          /    \
        num[i]  prevCount + 1
        '''
        # TC: O(n^2)
        # SC: O(n^2)
        @cache
        def dfs(idx, prevIdx):
            if idx == len(nums):
                return 0
            
            # 不选的话
            skip = dfs(idx+1, prevIdx)
            # 选
            take = 0
            if prevIdx == -1 or nums[idx] > nums[prevIdx]:
                take =  1 + dfs(idx+1, idx)
            
            return max(skip, take)
        
        return dfs(0, -1)

        # bottom up
        # 这里最主要的一个点就是subsequence
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[i+1])
        return max(dp)
