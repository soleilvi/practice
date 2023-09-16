'''
Python 3
https://leetcode.com/problems/top-k-frequent-elements/

By Soleil Vivero
09/16/23
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        d = sorted(d.items(), key = lambda x : x[1])  # d is now a list

        for i in range(k):
            l.append(d[-(i + 1)][0])  # retrieve what would be the dic-
                                      # tionary key starting from the 
                                      # end of the list

        return l