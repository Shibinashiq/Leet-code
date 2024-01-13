class Solution(object):
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
                 
        #how to checkk all the numbers i stays 0 index 
                    
        