class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        res = 0
        if len(nums) not in nums:
            return len(nums)
        elif 1 not in nums:
            return 1
        elif 0 not in nums:
            return 0
        else:
            if len(nums) % 2 == 0:
                sum1 = len(nums) * len(nums) // 2

            else:
                sum1 = (len(nums) + 1) * (len(nums) - 1) // 2 + (len(nums) + 1) // 2
        res = sum1 - sum(nums)
        return res