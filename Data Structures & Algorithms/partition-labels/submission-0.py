class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        题目要求把字符串切成尽可能多的区间，
        并且同一个字符只能出现在一个区间里。

        如果当前区间出现字符 c，
        那么这个区间必须至少延伸到 c 最后一次出现的位置。

        所以：
        1. 先记录每个字符最后一次出现的位置。
        2. 从左往右扫描，维护当前区间必须到达的最右边界 end。
        3. 当 i == end 时，说明当前区间里的所有字符都不会在后面再次出现，
           可以在这里切割。
        """

        last_pos = defaultdict()
        for i, c in enumerate(s):
            last_pos[c] = i

        start, end = 0, 0
        res = []
        for i, char in enumerate(s):
            end = max(end, last_pos[char])

            if i == end:
                res.append(end-start + 1)
                start = i + 1
        return res
        
