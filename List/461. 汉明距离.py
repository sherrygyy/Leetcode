class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        if len(x) <= len(y):
            x = (len(y) - len(x)) * "0" + x
        else:
            y = (len(x) - len(y)) * "0" + y
        count = 0
        i = 0
        while i < len(x):
            if x[i] != y[i]:
                count = count + 1
                i = i + 1
            else:
                i = i + 1
        return count