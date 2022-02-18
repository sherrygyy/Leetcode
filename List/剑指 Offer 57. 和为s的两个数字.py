class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i = 0
        j = len(nums) -1
        res = []
        while i < j:
            if nums[i] + nums[j] == target:
                res.append(nums[i])
                res.append(nums[j])
                return res
            else:
                if nums[i] + nums[j] > target:
                    j = j -1
                else:
                    i = i + 1