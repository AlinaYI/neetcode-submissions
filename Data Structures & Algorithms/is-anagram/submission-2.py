from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        for key, val in s_count.items():
            if val != t_count[key]:
                return False
        return True