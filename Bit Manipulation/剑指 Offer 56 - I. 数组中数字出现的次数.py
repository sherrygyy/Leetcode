class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        l = []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1

        for num in d:
            if d[num] == 1:
                l.append(num)
        return l