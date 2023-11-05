# Problem Statement:    https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/9lEkqOezpWw

class Solution:
    def reverseWords(self, s: str) -> str:
        
        return " ".join(reversed(s.split()))
