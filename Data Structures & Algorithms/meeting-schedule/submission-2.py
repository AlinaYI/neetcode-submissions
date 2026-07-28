"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda interval:interval.start)
        for i in range(1, len(intervals)):
            start = intervals[i].start
            pre_end = intervals[i-1].end

            if start < pre_end:
                return False
        return True