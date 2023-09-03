'''
Python 3
https://leetcode.com/problems/merge-sorted-array/

By Soleil Vivero
09/02/23
'''

nums1 = [0, 2, 5, 0, 8]
nums2 = [9, 5, 7, 8, 1]

def remove_zeroes(list):
    while 0 in list:
        list.remove(0)

def merge(list1, list2):
    list1 = sorted(list1 + list2)

def transform(list):
    list = [0, 9, 3, 4]

print(nums1)
remove_zeroes(nums1)
print(nums1)
merge(nums1, nums2)
print(nums1)
transform(nums1)
print(nums1)