class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        base, exampl2 if len(t) > len(s): return ""
        s:"XYXZ", t : "XYZ"
            |
        record pointer s

        Counter(t): freq for each letters
        tc: On, sc: On
        '''

        formed = 0
        window = {}
        res = float("inf"), None, None
        diction = Counter(t)
        count_t = Counter(t)
        r = l = 0

        while r < len(s):

            letter = s[r]
            window[letter] = window.get(letter, 0) + 1
            if letter in diction and window[letter] == diction[letter]:
                formed += 1

            # left pointer
            while l <= r and formed == len(diction):
                print(letter)
                letter = s[l]
                # length
                if r - l  + 1 < res[0]:
                    res = (r - l + 1, l, r)

                window[letter] -= 1
                if letter in diction and window[letter] < diction[letter]:
                    formed -= 1
                l += 1
            r += 1
        print(window)
        print(res)
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]
        
