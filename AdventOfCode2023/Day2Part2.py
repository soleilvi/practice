colorMaxVals = {'r': 0, 'g': 0, 'b': 0}
numAsStr = ""
totalSum = 0

with open("AdventOfCode2023/files/Day2.txt", 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    line = line.replace(f"Game {i + 1}:", "")

    for char in line:
        if char.isdigit():
            numAsStr += char
        if numAsStr and (char == 'r' or char == 'g' or char == 'b'):
            colorMaxVals[char] = max(colorMaxVals[char], int(numAsStr))
            numAsStr = ""

    totalSum += colorMaxVals['r'] * colorMaxVals['g'] * colorMaxVals['b']
    colorMaxVals['r'] = 0
    colorMaxVals['g'] = 0
    colorMaxVals['b'] = 0
    
print(totalSum)
