'''
Python 3
https://leetcode.com/problems/min-stack/

This problem took me a surprising amount of time, and taught me to fo-
llow my brainstorming ideas through to the end. I initially had the
right idea for the minimum values (to make it a stack), but after thi-
nking about it for a few seconds, I decided that it wouldn't work. If
I had stuck with it and illustrated it on paper instead of simply doi-
ng it my head, it would have saved me a couple hours.

By Soleil Vivero
11/23/23
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        if not self.minVals or self.minVals[-1] >= val:
            self.minVals.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minVals[-1]:
            self.minVals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]