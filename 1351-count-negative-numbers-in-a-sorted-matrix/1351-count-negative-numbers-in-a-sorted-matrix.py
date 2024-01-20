class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        lis=[]
        count=0
        for sublist in grid:
            for i in sublist:
                if i <0:
                    count+=1
        return count
            
        