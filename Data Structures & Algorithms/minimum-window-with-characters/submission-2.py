from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = Counter(t)
        missing = len(t)

        left = 0
        res_left = 0
        res_len = float("inf")

        for right in range(len(s)):
            char = s[right]

            # 当前字符还是我们缺少的
            if count[char] > 0:
                missing -= 1

            # 当前字符进入窗口
            count[char] -= 1

            # 已经包含 t 的所有字符，开始缩小
            while missing == 0:
                if right - left + 1 < res_len:
                    res_left = left
                    res_len = right - left + 1

                left_char = s[left]

                # 左边字符离开窗口
                count[left_char] += 1

                # 离开以后，我们重新缺少这个字符
                if count[left_char] > 0:
                    missing += 1

                left += 1

        if res_len == float("inf"):
            return ""

        return s[res_left:res_left + res_len]