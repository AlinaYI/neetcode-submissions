class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        def backtrack(start, comb, total):
            if total == target:
                res.append(comb[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # skip duplicate candidates at the same tree level.
                # 剪枝
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, comb, total + candidates[i])
                comb.pop()

        res = []
        backtrack(0, [], 0)
        return res