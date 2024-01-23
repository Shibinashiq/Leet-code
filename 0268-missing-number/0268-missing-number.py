class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0

     
        for i in range(len(nums)):
            a += nums[i]


        n = len(nums) + 1
        expected_sum = n * (n - 1) // 2

       
        missing_number = abs(expected_sum - a)

        return missing_number

        