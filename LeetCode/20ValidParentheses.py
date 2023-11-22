'''
Python 3
https://leetcode.com/problems/valid-parentheses/

By Soleil Vivero
11/21/23
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        if len(s) <= 1:
            return False

        for c in s:
            if (c == '('
            or c == '['
            or c == '{'):
                stack.append(c)
            elif len(stack) > 0:
                if abs(ord(c) - ord(stack.pop())) > 2:
                    return False

        return True
         