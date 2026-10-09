class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            keys = tuple(sorted(s))
            group[keys].append(s)
        return list(group.values())