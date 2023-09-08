'''
Python 3
https://leetcode.com/problems/group-anagrams/

By Soleil Vivero
09/08/23
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif s == t:
            return True
        else:
            count = defaultdict(int)

            for sChar, tChar in zip(s, t):
                count[sChar] += 1
                tDict[tChar] -= 1
            
            for val in count.values():
                if val != 0:
                    return False
            
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = []

        for i in range(len(strs)):
            cols = []
            cols.append(strs[i])
            for j in range(len(strs) + 1):  # Out of range
                if isAnagram(strs[i], strs[j]):
                    cols.append(strs[j])
                    # remove element
            # remove element
