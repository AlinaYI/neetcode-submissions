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

        intervals.sort(key=lambda key:key.start)
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end
            # overlap
            if currStart < intervals[i-1].end:
                return False
        return True