class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())

        # 前面的组 + 最后一组的nums
        lastRound = 0
        for key, freq in count.items():
            if freq == maxFreq:
                lastRound += 1
        
        res = (maxFreq-1)*(n+1) + lastRound
        return max(res, len(tasks))