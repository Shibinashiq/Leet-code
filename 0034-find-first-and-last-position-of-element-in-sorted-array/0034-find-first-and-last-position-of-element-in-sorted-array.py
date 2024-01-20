class Solution(object):
    def searchRange(self, nums, target):
        indices = []
        for i, number in enumerate(nums):
            if number == target:
                indices.append(i)
                
        if not indices:
            return [-1, -1]
        
        return [indices[0], indices[-1]]
