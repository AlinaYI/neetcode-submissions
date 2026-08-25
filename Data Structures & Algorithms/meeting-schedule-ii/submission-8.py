"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # 这里就是看需要多少个room
        # 可以用heap，如果有冲突的时候，取最早结束的会议
        # 让冲突的会议接着用最先腾出来的meeting room
        
        intervals.sort(key=lambda x:x.start)
        minHeap = [] # store endTime
        for i in range(len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end
            # 有冲突，如果heap里面最小的有冲突
            # 就要多加一个会议室
            if not minHeap or currStart < minHeap[0]:
                heapq.heappush(minHeap, currEnd)
            else:
                EarliestEnd = heapq.heappop(minHeap)
                heapq.heappush(minHeap, currEnd)
        return len(minHeap)