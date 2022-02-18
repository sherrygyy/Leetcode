class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        nums1 = []
        nums2 = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums2.append(nums[i])
            else:
                nums1.append(nums[i])
        return nums1 + nums2