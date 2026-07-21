class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, comb):
            if len(comb) == len(nums):
                res.append(comb[:])
                return

            for i in range(0, len(nums)):
                if nums[i] in comb:
                    continue
                
                comb.append(nums[i])
                backtrack(0, comb)
                comb.pop()

        res = []
        backtrack(0, [])
        return res