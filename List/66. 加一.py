class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = 0
        for i in range(len(digits)):
            val = val + digits[i] * 10 ** (len(digits) - 1 - i)
        val = val + 1
        val = str(val)
        ls = []
        for ch in val:
            ls.append(int(ch))
        return ls