class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            []
          /  |
         [2] [5]
         / \
        [2] [5] ...
        / \ 
       [2] [5] ..
       / \
    [2]  [5] ...
    / \
   [2] [5] ---

    backtrack 2^n
        '''

        def backtrack(start, comb, total):
            if total == target:
                res.append(comb[:])
                return

            if total > target:
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i, comb, total + nums[i])
                comb.pop()

        res = []
        backtrack(0, [], 0)
        return res