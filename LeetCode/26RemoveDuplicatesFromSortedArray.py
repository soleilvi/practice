'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

By Soleil Vivero
09/05/23
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums) - 1:
            if nums[i + 1] == nums[i]:
                nums.pop(i + 1)
            else:
                i += 1
            
        return len(nums)