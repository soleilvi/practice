'''
Python 3
https://leetcode.com/problems/remove-element/

By Soleil Vivero
09/04/23
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)