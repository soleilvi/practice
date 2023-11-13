'''
Fails when:
- There is only one number in the list
- There are only a couple numbers in the list
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0

        if len(s) == 1:
            return 1

        for num in s:
            if num + 1 in s or num - 1 in s:
                count += 1
        
        return count