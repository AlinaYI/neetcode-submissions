class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start, comb, currTotal):
            if currTotal == target:
                res.append(comb[:])
            
            if currTotal > target:
                return

            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i, comb, currTotal+nums[i])
                comb.pop()

        res = []
        backtrack(0, [], 0)
        return res