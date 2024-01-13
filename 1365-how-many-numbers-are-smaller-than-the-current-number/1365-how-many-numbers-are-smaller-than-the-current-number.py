class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        lis = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            lis.append(count)
        return lis
