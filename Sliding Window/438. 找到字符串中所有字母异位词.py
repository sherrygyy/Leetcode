class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = []
        d1 = {}
        d2 = {}
        if len(s) < len(p):
            return l

        for ch in p:
            if ch not in d1:
                d1[ch] = 1
            else:
                d1[ch] = d1[ch] + 1

        for ch in s[:len(p)]:
            if ch not in d2:
                d2[ch] = 1
            else:
                d2[ch] = d2[ch] + 1

        if d1 == d2:
            l.append(0)

        i = 0
        j = len(p) - 1
        while j+1 < len(s):
            if d2[s[i]] == 1:
                del d2[s[i]]
            else:
                d2[s[i]] = d2[s[i]] -1

            if s[j+1] not in d2:
                d2[s[j+1]] = 1
            else:
                d2[s[j+1]] = d2[s[j+1]] + 1

            if d1 == d2:
                l.append(i+1)
            i = i + 1
            j = j + 1

        return l