class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        # 如果当前需要的值多了
        # 那这里的count会是负数，要检查value
        need = Counter(t)
        needLen = len(t)
        
        res = ""
        left = 0
        for right in range(len(s)):
            
            rightChar = s[right]
            if rightChar in need and need[rightChar] > 0:
                needLen -= 1
            need[rightChar] -= 1

            # start shrink
            while needLen == 0:
                window = s[left:right+1]
                if not res or len(res) > len(window):
                    res = window
                
                leftChar = s[left]
                need[leftChar] += 1
                if leftChar in need and need[leftChar] > 0:
                    needLen += 1
                left += 1
        return res