class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        are_values_equal = len(set(dic.values())) == len(dic)
        return are_values_equal