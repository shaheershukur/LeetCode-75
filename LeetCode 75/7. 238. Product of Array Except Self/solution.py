# Problem Statement:    https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
# Visual Explanation:   https://youtu.be/V_De_bhXKzc

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [None for _ in range(len(nums))]

        leftProduct = 1
        for l in range(len(nums)):
            res[l] = leftProduct
            leftProduct *= nums[l]

        rightProduct = 1
        for r in range(len(nums)-1, -1, -1):
            res[r] *= rightProduct
            rightProduct *= nums[r]

        return res
