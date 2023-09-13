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

        for num in nums:
            d[num] += 1

        for i in range(k):
            n = max(d.values())
            l.append(n)
            d.pop()  # Somehow remove the element using n without sort

        return l