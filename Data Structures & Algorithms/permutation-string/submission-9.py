class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0]*26
        windows = [0]*26

        for i in range(len(s1)):
            need[ord(s1[i])-ord('a')] +=1
            windows[ ord(s2[i])-ord('a')] +=1
        if need == windows:
            return True
        
        left = 0
        for i in range(len(s1), len(s2)):
            windows[ ord(s2[i])-ord('a')] +=1
            windows[ ord(s2[left])-ord('a')] -=1
            if windows == need:
                return True
            left += 1
        return False