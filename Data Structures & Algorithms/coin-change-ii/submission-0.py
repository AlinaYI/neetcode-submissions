from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        decision tree
                []
          /     |   \
          1     2   3 --> 根据remaining再选之后的
       /  |  \  |    |
      1   2   3 2    3
     /   / \
    1   1   2
   /   /
  1   1

        '''

        # top-down
        @cache
        def dfs(idx, remain):
            if remain == 0:
                return 1
            
            if idx == len(coins) or remain < 0:
                return 0
            
            # choose
            choose = dfs(idx, remain-coins[idx])
            # skip
            skip = dfs(idx+1, remain)
            
            return choose+skip
        return dfs(0, amount)