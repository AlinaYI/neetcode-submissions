class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        # value < 0, 说明当前的char 多了
        # value == 0， 说明当前的char 正好
        # value > 0， 说明当前的char 少了
        needCharFreq = Counter(t)
        needLen = len(t)

        left = 0
        resLeft = 0
        resLen = float("inf")
        for right in range(len(s)):
            currChar = s[right]
            if currChar in needCharFreq and needCharFreq[currChar] >0:
                needLen -= 1
            needCharFreq[currChar] -= 1

            while needLen == 0:
                if resLen == float("inf") or right-left+1 < resLen:
                    resLeft = left
                    resLen = right-left+1
                
                leftChar = s[left]
                needCharFreq[leftChar] += 1
                if needCharFreq[leftChar] > 0:
                    needLen += 1
                left += 1
        return s[resLeft:resLeft+resLen] if resLen != float("inf") else ""