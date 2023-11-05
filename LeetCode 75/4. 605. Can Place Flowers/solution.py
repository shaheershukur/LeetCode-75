# Problem Statement:    https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/qIOGOcKRlJI

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if(n==0):
            return True

        planted = 0

        for i in range(len(flowerbed)):
            leftIsEmpty = (i == 0) or (flowerbed[i-1] == 0)
            rightIsEmpty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

            if(flowerbed[i] == 0 and leftIsEmpty and rightIsEmpty):
                flowerbed[i] = 1
                planted += 1

                if(planted == n):
                    return True

        return False
