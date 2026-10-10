class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needLen = len(t)
        # >0, still need
        # ==0, exactly what we need
        # <0, extra
        needChar = Counter(t)

        resLeft = 0
        resLen = None
        left = 0
        for right in range(len(s)):
            currChar = s[right]
            if currChar in needChar and needChar[currChar] > 0:
                needLen -= 1
            needChar[currChar] -= 1

            while needLen == 0:
                if resLen == None or resLen > right-left+1:
                    resLeft = left
                    resLen = right-left+1
                
                leftChar = s[left]
                needChar[leftChar] += 1
                left += 1
                if needChar[leftChar] > 0:
                    needLen += 1
        return s[resLeft:(resLen+resLeft)] if resLen else ""