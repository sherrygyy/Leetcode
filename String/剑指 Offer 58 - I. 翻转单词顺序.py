class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")
        s.reverse()
        res = ""
        for string in s:
            if len(string) > 0:
                res = res + string + " "

        return res[:-1]