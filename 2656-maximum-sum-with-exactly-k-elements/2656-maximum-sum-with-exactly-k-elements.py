class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        nums_copy = nums.copy()
        a=0
        for i in range(k):
            max_index = nums_copy.index(max(nums_copy))
            max_value = nums_copy[max_index]
            nums_copy[max_index] = max_value + 1
            a+=max_value
            
        
        return a