"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)
        minHeap = [intervals[0].end]
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end

            if currStart >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, currEnd)
        return len(minHeap)