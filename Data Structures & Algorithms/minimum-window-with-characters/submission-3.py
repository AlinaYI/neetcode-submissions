class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        这道题是要找到包含t的最小的window
        要求返回的是找到s中包含t的最小的substring

        思路就是先走right pointer，直到包含t里面的所有的char
        然后再缩小left，找到mimum的值
        '''
        # 如果t大，就不能有答案
        if len(t) > len(s):
            return ""
        
        # 用来记录right pointer要走到哪里
        count = Counter(t)
        stillNeed = len(t)

        left = 0
        res = ""

        for right, char in enumerate(s):
            # 如果当前这个值需要，并且可能还有需要的，mark
            if char in count and count[char] > 0:
                stillNeed -= 1

            count[char] -= 1
            
            while stillNeed == 0:
                window = s[left:right+1]

                if not res or len(window) < len(res):
                    res = window
                
                leftChar = s[left]
                count[leftChar] += 1
                # 左边这个字符被移出窗口以后，我们又开始缺这个字符了。
                if count[leftChar] > 0:
                    stillNeed += 1

                left += 1
        return res