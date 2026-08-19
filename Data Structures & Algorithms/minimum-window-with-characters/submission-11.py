from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        needCount = Counter(t)
        needLen = len(t)

        left = 0

        resLeft = 0
        resLen = float("inf")

        for right in range(len(s)):
            rightChar = s[right]

            if needCount[rightChar] > 0:
                needLen -= 1

            needCount[rightChar] -= 1

            while needLen == 0:
                # update answer
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    resLeft = left

                # shrink
                leftChar = s[left]
                needCount[leftChar] += 1

                if needCount[leftChar] > 0:
                    needLen += 1

                left += 1

        if resLen == float("inf"):
            return ""

        return s[resLeft:resLeft + resLen]