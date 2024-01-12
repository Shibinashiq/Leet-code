class Solution(object):
    def singleNumber(self, nums):
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        least_repeat=min(dic,key=dic.get)
        if dic[least_repeat]==1:
            
             return least_repeat
        else:
            None
        