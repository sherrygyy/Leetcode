class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        total = sum(nums[:k])
        temp = sum(nums[:k])
        for num in nums[k:]:
            temp = temp + num - nums[i]
            total = max(total,temp)
            i = i + 1
        return total / k