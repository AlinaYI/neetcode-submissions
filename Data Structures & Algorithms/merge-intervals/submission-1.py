class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []

        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            pre_start, pre_end = res[-1]
            curr_start, curr_end = intervals[i]

            if pre_end >= curr_start:
                res[-1][1] = max(pre_end, curr_end)
            else:
                res.append([curr_start, curr_end])
        return res

