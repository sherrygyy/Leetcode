class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        n = bin(n)[2:]
        if "1" not in str(n)[1:]:
            return True
        else:
            return False