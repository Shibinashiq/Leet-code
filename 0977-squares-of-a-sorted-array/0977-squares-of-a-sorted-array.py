class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lis=[]
        for i in nums:
            a= i *i
            lis.append(a)
        lis.sort()
        return lis