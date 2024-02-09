class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
     
        value=max(candies)
        lis=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >=value:
                lis.append(True)
            else:
                lis.append(False)
        return lis
                