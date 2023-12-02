colorMaxVals = {"r": 12, "g": 13, "b": 14}
gameIsValid = True
numAsStr = ""
totalSum = 0

with open("AdventOfCode2023/files/Day2.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    line = line.replace(f"Game {i + 1}:", "")

    for char in line:
        if char.isdigit():
            numAsStr += char
        if numAsStr and (char == 'r' or char == 'g' or char == 'b'):
            if int(numAsStr) > colorMaxVals[char]:
                gameIsValid = False
            numAsStr = ""

    if gameIsValid:
        totalSum += i + 1
    
    gameIsValid = True

print(totalSum)
