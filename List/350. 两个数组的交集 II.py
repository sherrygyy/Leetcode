# 两个数组的交集 II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = []
        if len(nums1) <= len(nums2):
            for num in nums1:
                if num in nums2:
                    list1.append(num)
                    nums2.remove(num)

        else:
            for num in nums2:
                if num in nums1:
                    list1.append(num)
                    nums1.remove(num)
        return list1