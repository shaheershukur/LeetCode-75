# Problem Statement:    https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/o0iRN12EC1g

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if (str1+str2) == (str2+str1):
            lengthOfCommonString = gcd(len(str1), len(str2))
            return str1[0:lengthOfCommonString]

        return ""
