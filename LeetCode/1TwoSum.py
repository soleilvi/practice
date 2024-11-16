'''
https://leetcode.com/problems/two-sum/

By Soleil Vivero
11/16/2024
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            x = target - num
            if x in hashmap:
                return [hashmap[x], i]
            else:
                hashmap[num] = i
