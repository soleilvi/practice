'''
Python 3
https://leetcode.com/problems/valid-parentheses/

By Soleil Vivero
11/22/23
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if (c == '('
            or c == '['
            or c == '{'):
                stack.append(c)
            else:
                # no beginning parenthesis
                if len(stack) == 0:
                    return False

                # closing parenthesis doesn't match
                elif abs(ord(c) - ord(stack.pop())) > 2:
                    return False

        # Beginning parenthesis without a closing one
        if len(stack) > 0:
            return False

        return True
         