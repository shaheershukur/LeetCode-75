# Problem Statement:    https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/uHYjUMR3Tg8

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        vowels = set('aeiouAEIOU')

        i, j = 0, len(s)-1

        while(i<j):
            if(s[i] not in vowels):
                i += 1
            elif(s[j] not in vowels):
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
