class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        needLen = len(t)
        need = Counter(t)

        left = 0
        resLeft = 0
        resLen = None
        for right in range(len(s)):
            currChar = s[right]
            if currChar in need and need[currChar] > 0:
                needLen -= 1
            need[currChar] -= 1

            while needLen == 0:
                if resLen == None or right-left+1 < resLen:
                    resLen = right-left+1
                    resLeft = left
                
                leftChar = s[left]
                need[leftChar] += 1
                if need[leftChar] > 0:
                    needLen += 1
                left += 1
        return s[resLeft:resLeft+resLen] if resLen != None else ""