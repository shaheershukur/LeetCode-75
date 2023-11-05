# Problem Statement:    https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/Vd-YX40Zz0Q

class Solution:
    def compress(self, chars: List[str]) -> int:
        r, i = 0, 0

        while(i < len(chars)):
            currChar = chars[i]
            currOcc = 0
            while((i < len(chars)) and (chars[i] == currChar)):
                currOcc += 1
                i += 1

            chars[r] = currChar
            r += 1
            if(currOcc > 1):
                currOccStr = str(currOcc)
                for j in range(len(currOccStr)):
                    chars[r] = currOccStr[j]
                    r += 1

        return r
