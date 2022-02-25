class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] == 1:
            return 0
        if len(nums) not in nums:
            return len(nums)
        i = 1
        res = nums[0]-1
        while i < len(nums):
            if nums[i] - nums[i-1] == 2:
                res = nums[i] - 1
            i = i + 1
        return res