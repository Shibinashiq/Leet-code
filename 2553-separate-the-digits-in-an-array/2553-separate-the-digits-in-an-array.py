class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string = ''.join(map(str, nums))
        lis = []
        for i in string:
            lis.append(int(i))
        return lis