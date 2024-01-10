class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i<len(nums):
            j=i+1
            while j <len(nums):
                if nums[i]==nums[j]:
                    del nums[j]
                else:
                    j+=1
            i+=1
        

    
    