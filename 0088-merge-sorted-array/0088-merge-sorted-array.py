class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_part = nums1[:m]
        nums2_part = nums2[:n]

        nums1[:m + n] = sorted(nums1_part + nums2_part)