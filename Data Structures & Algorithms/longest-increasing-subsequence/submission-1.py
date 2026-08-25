from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        这里需要make 的decision就是选择当前的数字加入之前还是新开一个increased subsequence
            []
          /    \
        num[i]  prevCount + 1
        '''
        
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
