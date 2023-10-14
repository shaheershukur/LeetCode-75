# Problem Statement:    https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/pXAvwRyJ0dw

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = [False for _ in range(len(candies))]

        currentGreatestCandies = max(candies)

        for i, currentCandies in enumerate(candies):
            if(currentCandies+extraCandies >= currentGreatestCandies):
                result[i] = True

        return result
