class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common_factors = set()
        for i in range(1,min(a,b)+1):
            if a % i == 0 and b % i == 0:
                common_factors.add(i)
        
        return len(common_factors)

                
        
        