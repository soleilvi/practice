'''
Python 3
https://leetcode.com/problems/majority-element/

By Soleil Vivero
09/06/23
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        noRepeatsNums = set(nums)

        for num in noRepeatsNums:
            if nums.count(num) > len(nums)/2:
                return num
