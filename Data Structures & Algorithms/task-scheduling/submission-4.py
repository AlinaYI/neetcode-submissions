class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # X Y _ X Y _
        # total round = maxFreq
        # length of each round: n + 1
        # total element: len(count.keys())
        # last round， freq == maxfreq

        count = Counter(tasks)
        maxFreq = max(count.values())
        maxCount = 0
        for freq in count.values():
            if freq == maxFreq:
                maxCount += 1

        res = 0
        res += (maxFreq - 1)*(n+1) + maxCount
        return max(res, len(tasks))