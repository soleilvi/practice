'''
Python 3
https://leetcode.com/problems/longest-consecutive-sequence/

By Soleil Vivero
11/20/23
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 1
        longest = 0

        for num in s:
            if num - 1 not in s:
                # Still O(n) because worst-case scenario, the algorit-
                # hm runs through the set twice
                while num + 1 in s:
                    count += 1
                    num += 1
                    
                if count > longest:
                    longest = count
            
            count = 1

        return longest
                     
        