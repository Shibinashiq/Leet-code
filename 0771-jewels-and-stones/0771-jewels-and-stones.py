class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        dic={}
        count=0
        for i in jewels:
            for j in stones:
                if i == j:
                    count+=1
        return count
                    
        