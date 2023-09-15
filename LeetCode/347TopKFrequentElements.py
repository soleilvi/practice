'''
Python 3
https://leetcode.com/problems/top-k-frequent-elements/

By Soleil Vivero
09/15/23
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(int)
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        minListNum = d[nums[0]]  # Get the value of the first item in the 
                                 # dictionary (python 3.7 and onward)

        for key in d:
            if len(s) < k:
                s.append(key)

                if d[key] < minListNum:
                    minListNum = d[key] 
    
            else:
                if d[key] > minListNum:
                    s[len(s) % k] = key

        return s