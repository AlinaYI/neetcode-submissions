class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        # maintain preEnd, 用来对比，如果要remove的话，
        # 更希望保存的是更小的preEnd，这样就能最小话需要remove的intervals
        preEnd = intervals[0][1]
        removed = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # overlap, need remove
            if start < preEnd:
                removed += 1
                preEnd = min(end, preEnd)
            else:
                preEnd = end
        return removed
