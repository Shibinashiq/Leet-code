class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result_set = set()

        for num in set(nums1):
            if num in nums2 or num in nums3:
                result_set.add(num)

        for num in set(nums2):
            if num in nums1 or num in nums3:
                result_set.add(num)

        for num in set(nums3):
            if num in nums1 or num in nums2:
                result_set.add(num)

        return list(result_set)