class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        X Y _ X Y
        
        X * (1+3),  + x+y

        Counter(tasks)

        X Y _ _ X Y _ _ n = 3

        total round: maxfreq(All key)
        each round length: n+1 
        lastround = key type
        sum = maxfreq(All key)-1 * (n+1) + len(all key)

        每次拿最大的freq， maxHeap
        '''
        count = Counter(tasks)
        maxHeap = []
        for key, freq in count.items():
            heapq.heappush(maxHeap, (-freq, key))

        maxFreq, key = heapq.heappop(maxHeap)
        maxFreq = -1 * maxFreq
        # maxFreq = heapq.nlargest(1, count.values, count.keys())
        curr = (maxFreq-1) * (n+1) + 1

        while maxHeap:
            curr_freq, key = heapq.heappop(maxHeap)
            curr_freq *= -1

            if maxFreq == curr_freq:
                curr += 1
        return max(curr, len(tasks))