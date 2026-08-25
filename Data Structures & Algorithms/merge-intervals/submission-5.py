class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        prevStart, prevEnd = intervals[0]
        res = []

        for currStart, currEnd in intervals[1:]:
            
            # overlap
            if currStart <= prevEnd:
                prevEnd = max(prevEnd, currEnd)

            # non-overlap
            else:
                res.append( [prevStart, prevEnd] )
                prevStart, prevEnd = currStart, currEnd

        res.append( [prevStart, prevEnd] )
        return res