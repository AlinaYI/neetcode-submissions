class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        needLen = len(t)
        # 这里记录的是所有需要字符的freq
        # 如果 freq < 0, 说明多出来了，那么needLen就不用减少了
        needNum = Counter(t)
        res = ""
        left = 0
        for right in range(len(s)):

            currChar = s[right]
            if currChar in needNum and needNum[currChar] > 0:
                needLen -= 1
            needNum[currChar] -= 1
            
            while needLen == 0:
                window = s[left:right+1]
                if not res or len(res) > len(window):
                    res = window
                
                leftChar = s[left]
                needNum[leftChar] += 1
                if needNum[leftChar] > 0:
                    needLen += 1
                left += 1
        return res
                