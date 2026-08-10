class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        1. new 在 interval 左边
        newEnd < start
        → 后面都不用看了，直接返回

        2. interval 在 new 左边
        end < newStart
        → interval 放进 res

        3. overlap
        → merge 到 newInterval
        '''
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