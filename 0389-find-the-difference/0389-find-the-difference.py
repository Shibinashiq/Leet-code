class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic={}
        a=s+t
        # if len(set(a))==1:
        #     return a
            
        for i in a:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,value in dic.items():
            if value % 2 != 0:
                return key
        