class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lis=[]
        n=len(heights)
        for i in range(n):
            max_index=heights.index(max(heights))
            name=names[max_index]
            lis.append(name)
            heights.pop(max_index)
            names.pop(max_index)
        return lis
            

        