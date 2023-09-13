'''
Python 3
https://leetcode.com/problems/top-k-frequent-elements/

By Soleil Vivero
09/12/23
'''

# Maybe I can somehow use the Boyer-Moore majority voting algorithm?
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        mostFrequent = -1
        votes = 0

        for num in nums:
            if votes == 0:
                mostFrequent = num
                votes = 1
                l.insert(len(l) % k, num)
            
            if num == mostFrequent:
                votes += 1
            else:
                votes -= 1

        return l