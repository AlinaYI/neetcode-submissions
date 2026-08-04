class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            # [a..b] [c..d] 
            # overlap
            currStart, currEnd = intervals[i]
            if currStart <= res[-1][1]:
                res[-1][0] = min(res[-1][0], currStart)
                res[-1][1] = max(res[-1][1], currEnd)
            
            else:
                res.append(intervals[i])
        return res