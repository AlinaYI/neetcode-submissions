class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        count = Counter(t)
        stillNeed = len(t)
        left = 0
        res = ""
        for right, char in enumerate(s):

            if char in count and count[char] > 0:
                stillNeed -= 1

            count[char] -= 1
            while stillNeed == 0:
                window = s[left:right+1]
                if not res or len(window) < len(res):
                    res = window
                
                leftChar = s[left]
                count[leftChar] += 1
                if count[leftChar] > 0:
                    stillNeed += 1
                left += 1
        return res