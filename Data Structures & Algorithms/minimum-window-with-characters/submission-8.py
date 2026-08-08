class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        count = Counter(t)
        needLength= len(t)
        left = 0
        res = ""

        for right in range(len(s)):
            char = s[right]
            if char in count and count[char] > 0:
                needLength -= 1
            count[char] -= 1

            # 可以开始shrink窗口了
            while needLength == 0:
                window = s[left:right+1]
                if not res or len(res) > len(window):
                    res = window
                count[s[left]] += 1
                if count[s[left]] > 0:
                    needLength += 1
                left += 1
        return res