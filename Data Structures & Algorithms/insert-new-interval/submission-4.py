class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for i, (start, end) in enumerate(intervals):
            # [newInterval] [interval]
            if newInterval[1] < start:
                return res + [newInterval] + intervals[i:]

            # [interval]  [newInterval]
            elif newInterval[0] > end:
                res.append( [start, end] )
            
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        res.append(newInterval)
        return res