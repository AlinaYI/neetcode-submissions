class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groupMap[key].append(s)
        return list(groupMap.values())