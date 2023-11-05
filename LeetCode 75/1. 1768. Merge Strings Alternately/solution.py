# Problem Statement:    https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/CJEVZqjEddc

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0

        while (i<len(word1)) and (j<len(word2)):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        while (i<len(word1)):
            res.append(word1[i])
            i += 1

        while (j<len(word2)):
            res.append(word2[j])
            j += 1

        return "".join(res)