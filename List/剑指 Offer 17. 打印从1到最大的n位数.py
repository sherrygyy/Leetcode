class Solution:
    def printNumbers(self, n: int) -> List[int]:
        l = []
        for i in range(10**n-1):
            l.append(i+1)

        return l