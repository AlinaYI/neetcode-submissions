class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        这里就是有个容错率，也就是用counter记录一下不一样的字母频率
        也就是从left开始go through的时候，只要这个combination里面的字母最小的freq < k就满足
        '''

        count = defaultdict(int)
        left = res = 0
        maxfreq = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxfreq = max(maxfreq, count[s[right]])

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res