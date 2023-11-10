# Problem Statement:    https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/Tt3poT5qOqI

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i, j = 0, 0

        while(j < len(nums)):
            if(nums[j] != 0):
                nums[i] = nums[j]
                i += 1
            j += 1

        while(i < len(nums)):
            nums[i] = 0
            i += 1
