class Solution:
    def isFascinating(self, n: int) -> bool:
        a = '192384576'
        lis = []
        dic = {}
        b = n * 2
        c = n * 3

        lis.append(str(b))
        lis.append(str(c))
        lis.append(str(n))
        lis.sort()
        string = ''.join(lis)

        for i in string:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
                
        for i in range(1,10):
            a=str(i)
            digit_count=dic.get(a,0)
            if digit_count!=1:
                return False
        return True
            

                
            

        
        