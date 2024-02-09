class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lis1 = list(word1)
        lis2 = list(word2)
        lis3 = []

        max_len = max(len(lis1), len(lis2))

        for i in range(max_len):
            if i < len(lis1):
                lis3.append(lis1[i])
            if i < len(lis2):
                lis3.append(lis2[i])

        result = ''.join(lis3)

        return result

        