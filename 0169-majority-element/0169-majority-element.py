class Solution(object):
    def majorityElement(self, nums):
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        most_repeated=max(dic,key=dic.get)
        return most_repeated