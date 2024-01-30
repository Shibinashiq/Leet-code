class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for value in dic.values():
            if value % 2 != 0:
                return False

        return True