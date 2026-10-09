class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        countS = Counter(s)
        countT = Counter(t)
        for key, freq in countS.items():
            if freq != countT[key]:
                return False
        return True