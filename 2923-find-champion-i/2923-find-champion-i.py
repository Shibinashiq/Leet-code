class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        count=0
        lis=[]
        for i in grid:
            count=0
            for j in i:
                if j ==1:
                    count+=1
            lis.append(count)
        return lis.index(max(lis))
                    
            
        