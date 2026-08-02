class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # total round: n
        # each round length: n+1
        # round time: maxFreq
        # but last round cant be smaller: length(all key)

        count = Counter(tasks)
        maxFreq = max(count.values())
        maxCount = sum(freq == maxFreq for freq in count.values())
        curr = (maxFreq-1)*(n+1) + maxCount

        # bottom 是 len(tasks)
        return max(curr, len(tasks))