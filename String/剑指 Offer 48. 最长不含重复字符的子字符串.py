def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    j = 0
    res = 0
    while j < len(s):
        if s[j] not in d:
            d[s[j]] = j
            j = j + 1
            res = res + 1
        else:
            i = d[s[j]]
            d[s[j]] = j
            j = j + 1
    return res

a = "pwwkew"
b = lengthOfLongestSubstring(a)
print(b)