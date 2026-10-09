class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        windows = [0]*26
        target = [0]*26

        for i in range(len(s1)):
            target[ ord(s1[i]) - ord('a') ] += 1
            windows[ ord(s2[i]) - ord('a') ] += 1
        
        if target == windows:
            return True
        
        left = 0
        right = len(s1)
        while right < len(s2):
            windows[ ord(s2[right]) - ord('a') ] += 1
            windows[ ord(s2[left]) - ord('a') ] -= 1

            if windows == target:
                return True
            
            right += 1
            left += 1
        return False
        