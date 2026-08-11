class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # totalRound = maxFreq
        count = Counter(tasks)
        maxFreq = max(count.values())

        lastRound = 0
        for key, freq in count.items():
            if freq == maxFreq:
                lastRound += 1
        
        res = (maxFreq-1)*(n+1) + lastRound
        # 其他 task 足够多，可以把 idle 全填掉
        # 就会出现res < len(tashs)的情况
        return max(res, len(tasks))