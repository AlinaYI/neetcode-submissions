class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS = Counter(s)
        countT = Counter(t)

        for char,freq in countS.items():
            if countT[char] != freq:
                return False
        return True