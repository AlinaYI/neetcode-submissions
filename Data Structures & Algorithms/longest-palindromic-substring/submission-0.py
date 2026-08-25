class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        '''
        这道题是要最长的palindrom的substring
        这里有两种，
        1. 就是偶数， left = right = i
        2. 奇数， left = 1, right = i + 1

        每个 palindrome 一定有一个 center，所以枚举 center，再向两边扩。
        tc: O(n²)
        sc: O1
        '''

        def expand(left, right):
            while left >= 0  and right <=len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            # 注意这里
            # 退出 while 时，left/right 已经多走了一步
            return s[left + 1:right]

        res = ""
        for i in range(len(s)):
            
            # odd
            odd = expand(i,i)
            
            # even
            even = expand(i, i+1)

            res = max(even, odd, res, key = len )
            
        return res