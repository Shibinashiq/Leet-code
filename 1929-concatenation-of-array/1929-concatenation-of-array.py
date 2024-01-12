class Solution(object):
    def getConcatenation(self, nums):
        nums1=nums[:]
        n=len(nums1)
        nums=nums[:n]+nums1
        return nums
        