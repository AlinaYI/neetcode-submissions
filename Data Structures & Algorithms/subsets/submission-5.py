class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, comb):
            res.append(comb[:])

            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()

        res = []
        backtrack(0, [])
        return res