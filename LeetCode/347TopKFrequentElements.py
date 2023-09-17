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
    
'''
Since I couldn't come up with a solution with a time complexity better 
than O(nlog(n)) on my own, I watched a video
(https://www.youtube.com/watch?v=YPTqKIgVk-k) explaining a O(n) soluti-
on for this problem. Here is my attempt at solving it after hearing the
explanation without looking at the instructor's code:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMostRepeated = []
        countFrequency = defaultdict(int)
        groupByFrequency = defaultdict(list)

        # countFrequency: Count how many times a number appears in nums
        # groupByFrequency: Initialize keys so that they are in order
        for i in range(len(nums)):
            countFrequency[nums[i]] += 1 
            groupByFrequency[i] = []

        # The value of countFrequency is the key of groupByFrequency.
        # groupByFrequency has lists because some keys in countFrequen-
        # cy might have the same value.
        for key in countFrequency:
            groupByFrequency[countFrequency[key]].append(key)

        for i in range(len(nums)):
            for num in groupByFrequency[len(nums) - i]:  # Go backwards
                if len(kMostRepeated) >= k:
                    break
                kMostRepeated.append(num)
                 
        return kMostRepeated

        
Compare this to his code:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


I could have saved time by returning in the nested for-loop and memory
by making my second dictionary a 2D list.
'''