class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            hashmap[key].append(strs[i])
        
        return list(hashmap.values())