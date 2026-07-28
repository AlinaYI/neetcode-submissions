class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_count = Counter(s)
        t_count = Counter(t)

        for char, fre in s_count.items():
            if fre != t_count[char]:
                return False
        return True

