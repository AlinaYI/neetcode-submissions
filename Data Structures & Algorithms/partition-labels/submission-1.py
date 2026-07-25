class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # bfs level extension

        idex_map = defaultdict(int)
        for i, char in enumerate(s):
            idex_map[char] = i
        
        print(idex_map)

        start = 0
        curr_end = 0
        res = []
        for idx, char in enumerate(s):
            curr_end = max(curr_end, idex_map[char])

            if idx == curr_end:
                res.append(curr_end - start + 1)
                start = curr_end + 1

        return res