class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        for ch in nums:
            if ch not in dict1:
                dict1[ch] = 1
            else:
                dict1[ch] = dict1[ch] + 1
        for num in dict1:
            if dict1[num] > len(nums)/2:
                return num

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

