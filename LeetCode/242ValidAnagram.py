'''
Python 3
https://leetcode.com/problems/valid-anagram/

By Soleil Vivero
09/01/23
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif s == t:
            return True
        else:
            sDict = {}
            tDict = {}

            # Iterate through both strings simultaneously and count how 
            # often their characters appear. If they appear the same
            # amount of times, they are anagrams.
            for sChar, tChar in zip(s, t):
                if sChar not in sDict:
                    sDict[sChar] = 1
                else:
                    sDict[sChar] += 1

                if tChar not in tDict:
                    tDict[tChar] = 1
                else:
                    tDict[tChar] += 1
            
            if sDict == tDict:
                return True
            else:
                return False