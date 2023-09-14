'''
Python 3
https://leetcode.com/problems/top-k-frequent-elements/

By Soleil Vivero
09/12/23
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        d = defaultdict(int)
        previousKey = -1

        for num in nums:
            d[num] += 1

        for key in d:
            if d.get(key) > d.get(previousKey, 0):  # I really thought this would work ;-;
                l.insert(len(l) % k, key)
            
            previousKey = key

        return l