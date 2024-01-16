class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}

        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

       
        return len(set(dic.values())) == 1