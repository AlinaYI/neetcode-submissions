class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list) # key:tuple(sorted(s))
        for s in strs:
            key = tuple(sorted(s))
            hashmap[key].append(s)
        return list(hashmap.values())