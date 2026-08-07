class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0]*26
        window = [0]*26

        for idx, c in enumerate(s1):
            need[ord(c)-ord('a')] += 1
            window[ord(s2[idx]) - ord('a')] += 1
        
        if need == window:
            return True

        left= 0
        for right in range(len(s1), len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            window[ ord(s2[left]) - ord('a')] -= 1
            left += 1
            if window == need:
                return True
        return False