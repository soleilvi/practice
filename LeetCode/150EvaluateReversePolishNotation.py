'''
Python 3
https://leetcode.com/problems/evaluate-reverse-polish-notation/

By Soleil Vivero
11/24/23
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())

            elif token == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)

            elif token == '*':
                stack.append(stack.pop() * stack.pop())

            elif token == '/':
                num2 = stack.pop()
                num1 = stack.pop()

                if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
                    stack.append(num1 // num2 + (abs(num1) % abs(num2) > 0))
                else:
                    stack.append(num1 // num2)
                    
            else:
                stack.append(int(token))

        return stack[0]
