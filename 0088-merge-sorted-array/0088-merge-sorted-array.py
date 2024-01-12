class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Create copies of the relevant portions of nums1 and nums2
        nums1_part = nums1[:m]
        nums2_part = nums2[:n]

        # Merge the two arrays
        nums1[:m + n] = sorted(nums1_part + nums2_part)