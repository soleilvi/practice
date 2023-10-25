'''
Python 3
https://leetcode.com/problems/product-of-array-except-self/

By Soleil Vivero
10/25/2023
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        x = nums[0]

        for i in range(1, len(nums)):
            res.append(x)
            x *= nums[i]
        
        x = nums[-1]

        for i in range(len(nums) - 2):
            res[len(nums) - 1 - (i + 1)] *= x
            x *= nums[len(nums) - 1 - (i + 1)]
        
        res[0] = x

        return res