class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        这里是combination sum
        这里就是要加上所有的数字，可以重复
        然后sum == target
        '''

        def backtrack(start, comb):
            if sum(comb) == target:
                res.append(comb[:])

            if sum(comb) > target:
                return 

            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i, comb)
                comb.pop()   

        res = []
        backtrack(0, [])
        return res