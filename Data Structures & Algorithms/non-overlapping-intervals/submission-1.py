class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        removes = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                removes += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        return removes

# sorted by end
        intervals.sort(key=lambda interval:interval[1])
        keep = 0
        pre_end = float("inf")

        for start, end in intervals:
            if start >= pre_end:
                keep += 1
                prev_end = end
        return len(intervals) - keep