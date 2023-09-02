'''
Python 3
https://leetcode.com/problems/contains-duplicate/

By Soleil Vivero
09/01/23
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsInArr = set(nums)  # Replicate list as a set

        # Since sets can't have duplicate items, the set will have to
        # be shorter than the array if it has duplicate numbers
        if len(numsInArr) < len(nums):
            return True
        else:
            return False
