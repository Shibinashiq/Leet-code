class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        lis = []
        n = len(code)

        for i in range(n):
            current_sum = 0
            if k > 0:
                for j in range(1, k + 1):
                    current_sum += code[(i + j) % n]
                lis.append(current_sum)
            elif k < 0 :
                for j in range(k, 0, 1):
                    current_sum += code[(i + j) % n]
                lis.append(current_sum)
            else:
                 lis.append(0)
                # return lis
        return lis
            
            
                
            
        