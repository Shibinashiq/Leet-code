class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[]
        for i in range(1,n+1):
            if n % i==0:
                lis.append(nums[i-1] ** 2)
        return sum(lis)
            
        