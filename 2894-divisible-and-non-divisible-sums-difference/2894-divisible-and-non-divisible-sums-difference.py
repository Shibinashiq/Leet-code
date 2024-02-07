class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        lis = []
        sum_of_divisible = 0
        sum_of_all = 0
        for i in range(1, n+1):
            sum_of_all += i
            if i % m == 0:
                lis.append(i)
        sum_of_divisible = sum(lis)
        return sum_of_all - (2 * sum_of_divisible)

        