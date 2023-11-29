'''
Python 3
https://leetcode.com/problems/generate-parentheses/

By Soleil Vivero
11/29/23
'''

from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque(')' * n)
        stack = deque('(' * n)
        completeParentheses = ""
        final = [''.join(stack + queue)]

        while len(stack) > 1 and len(queue) > 1:
            if queue[-2] == '(':
                completeParentheses += "()"
                queue.pop()
                queue.pop()
                queue.append(stack.pop())
            else:
                queue.appendleft(stack.pop())
                stack.append(queue.pop())

            final.append(completeParentheses + ''.join(stack + queue))
        
        return final