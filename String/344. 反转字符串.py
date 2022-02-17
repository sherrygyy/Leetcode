class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        str1 = ""
        for i in range(len(s)-1, -1, -1):
            str1 = str1 + s[i] + "/"
        s[:] = str1.split("/")
        s.pop()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        h=len(s)//2
        for i in range(h):
            s[i],s[~i]=s[~i],s[i]

