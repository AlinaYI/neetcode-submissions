class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        count = Counter(tasks)
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        max_freq, key = heapq.heappop(heap)
        max_freq = (max_freq  * -1)
        # X _ _, X 
        curr_length = ((max_freq - 1) * (n + 1)) +  1

        while heap:
            curr_freq, key = heapq.heappop(heap)
            curr_freq = curr_freq * -1

            if max_freq == curr_freq:
                curr_length += 1
        return max(curr_length, len(tasks))
