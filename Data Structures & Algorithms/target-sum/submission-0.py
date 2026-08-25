from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        这里就是根据给的list然后算target
        这里只有加减

                2
             /    \
            +      -
            /       \
          2+2        2-2
          /  \      /   \       
         +    -    +     -
      2+2+2 2+2-2  2-2+2 2-2-2
        '''

        @cache
        def dfs(idx, currRes):
            if idx == len(nums):
                return 1 if currRes == target else 0
            
            return dfs(idx+1, currRes+nums[idx]) + dfs(idx+1, currRes-nums[idx])

        return dfs(0, 0)