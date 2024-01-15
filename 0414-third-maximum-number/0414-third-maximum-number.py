class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        if len(nums_set) >= 3:
            nums_set.remove(max(nums_set))
            nums_set.remove(max(nums_set))
            return max(nums_set)
        else:
            return max(nums_set)
                
            
            
            
       