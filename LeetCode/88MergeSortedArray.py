'''
Python 3
https://leetcode.com/problems/merge-sorted-array/

By Soleil Vivero
09/02/23
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while 0 in nums1:
            nums1.remove(0)
        
        while 0 in nums2:
            nums2.remove(0)

        nums1 = sorted(nums1 + nums2)
        print(nums1)