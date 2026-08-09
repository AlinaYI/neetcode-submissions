class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # [satrt, end], [start1, end1]
        # start1 < end -> overlap, remove += 1
        intervals.sort()
        remove = 0

        preEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]

            if currStart < preEnd:
                remove += 1
                preEnd = min(preEnd, currEnd)
            else:
                preEnd=currEnd
        return remove

