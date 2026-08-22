class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # need[c] > 0   → 还缺 c
        # need[c] == 0  → c 数量刚刚好
        # need[c] < 0   → c 多出来了
        need = Counter(t)
        needLen = len(t)

        left = 0
        resleft = 0
        resLen = float("inf")

        for right in range(len(s)):
            currChar = s[right]
            if currChar in need and need[currChar] > 0:
                needLen -= 1
            need[currChar] -= 1

            while needLen == 0:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    resLeft = left
                
                leftChar = s[left]
                need[leftChar] += 1
                if need[leftChar] > 0:
                    needLen += 1
                left += 1
        if resLen == float("inf"):
            return ""
        
        return s[resLeft:resLeft+resLen]
