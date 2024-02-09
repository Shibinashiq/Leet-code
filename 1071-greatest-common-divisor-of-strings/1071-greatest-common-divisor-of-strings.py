class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        concat1 = str1 + str2
        concat2 = str2 + str1

        if concat1 != concat2:
            return ''
        else:
            len1 = len(str1)
            len2 = len(str2)
            gcd1 = gcd(len1, len2)
            return str1[:gcd1]