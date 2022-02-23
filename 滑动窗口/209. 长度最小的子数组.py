class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        res = len(nums) + 1
        temp = 0
        for j in range(len(nums)):
            temp = temp + nums[j]
            while temp >= target:
                res = min(res, j - i + 1)
                temp = temp - nums[i]
                i = i + 1
        if res == len(nums) + 1:
            return 0
        else:
            return res