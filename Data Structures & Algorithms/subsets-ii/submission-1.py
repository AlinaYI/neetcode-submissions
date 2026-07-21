class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(start, comb):
            res.append(comb[:])

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()
                
        res = []
        backtrack(0, [])
        return res