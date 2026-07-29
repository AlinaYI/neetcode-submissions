class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for s in strs:
            temp = tuple(sorted(s))
            hashmap[temp].append(s)
        return list(hashmap.values())