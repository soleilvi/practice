'''
Python 3
https://leetcode.com/problems/generate-parentheses/

I couldn't solve this problem without help. I used this explanation
(https://www.youtube.com/watch?v=s9fokUqJ76A) to solve it. I didn't 
know about backtracking prior to this problem, so I learned a lot from 
it.

By Soleil Vivero
04/11/2024
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(openN, closeN):            
            if openN == n and closeN == n:
                result.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
            
        backtrack(0, 0)
        return result