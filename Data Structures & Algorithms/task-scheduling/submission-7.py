class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # total round: maxFreq
        # 只需要计算 total-1 round + max_freq的num
        # each round: n+1 length

        count = Counter(tasks)
        totalRound = max(count.values())

        res = 0
        res += (totalRound - 1)*(n+1)

        for key, freq in count.items():
            if freq == totalRound:
                res += 1
        return max(res, len(tasks))