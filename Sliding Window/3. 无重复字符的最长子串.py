class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        i = -1
        for j in range(len(s)):
            if s[j] in d:
                i = max(i, d[s[j]])
            d[s[j]] = j
            res = max(res, j - i)
        return res