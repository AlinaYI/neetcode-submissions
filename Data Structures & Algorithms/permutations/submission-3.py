class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
            
            for i in range(len(nums)):
                if nums[i] in comb:
                    continue

                comb.append(nums[i])
                backtrack(comb)
                comb.pop()

        res = []
        backtrack([])
        return res