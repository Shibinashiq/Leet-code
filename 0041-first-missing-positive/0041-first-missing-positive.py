class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums1,k=set(nums),1
        while k in nums1:
            k+=1
        return k