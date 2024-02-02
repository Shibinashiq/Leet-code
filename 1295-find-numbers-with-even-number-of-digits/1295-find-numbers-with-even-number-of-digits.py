class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        a = []
        
        for num in nums:
            a.append(len(str(num)))
        
        for i in a:
            if i % 2 == 0:
                count += 1
        
        return count