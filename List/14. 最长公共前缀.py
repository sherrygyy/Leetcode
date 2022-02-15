
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        if len(strs) > 1:
            if len(first) <= len(last):
                for i in range(len(first)):
                    if first[i] == last[i]:
                        res = res + first[i]
                    else:
                        break
            else:
                for i in range(len(last)):
                    if last[i] == first[i]:
                        res = res + last[i]
                    else:
                        break
        elif len(strs) == 1:
            res = strs[0]


        return res