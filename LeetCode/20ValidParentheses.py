'''
Python 3
https://leetcode.com/problems/valid-parentheses/

By Soleil Vivero
11/22/23
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if (c == '('
            or c == '['
            or c == '{'):
                stack.append(c)
            else:
                # stack is empty, there are no beginning parentheses
                if not stack:
                    return False

                # closing parenthesis doesn't match
                elif abs(ord(c) - ord(stack.pop())) > 2:
                    return False

        # stack isn't empty, we're missing a closing parenthesis
        if stack:
            return False

        return True
         