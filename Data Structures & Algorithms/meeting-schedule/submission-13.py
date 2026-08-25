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
        
        intervals.sort(key=lambda x:x.start)
        # 这里就是看有没有overlap
        # 如果有overlap的话，就是false
        prevStart = intervals[0].start
        prevEnd = intervals[0].end

        for i in range(1, len(intervals)):
            currStart = intervals[i].start
            currEnd = intervals[i].end

            if currStart < prevEnd:
                return False
            prevEnd = currEnd
        return True
