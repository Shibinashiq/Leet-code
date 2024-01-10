class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if val == nums[i]:
                del nums[i]
            else:
                i+=1

        print(nums) 