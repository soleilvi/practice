'''
Python 3
https://leetcode.com/problems/merge-sorted-array/

By Soleil Vivero
09/03/23
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for num in nums1[m:]:
            nums1.remove(num)

        nums1.extend(nums2[:n])
        nums1.sort()