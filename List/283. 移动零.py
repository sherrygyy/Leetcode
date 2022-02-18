class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while i < len(nums):
            if nums[i-count] == 0:
                nums.append(nums.pop(i-count))
                i = i + 1
                count = count + 1
            else:
                i = i + 1
