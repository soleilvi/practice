gearPairs = {}  # Key = gear index, Value = list of numbers adjacent to it
gearIndex = (0, 0)
numIsAdjacent = False
numAsStr = ""
totalSum = 0

with open("AdventOfCode2023/files/Day3.txt", "r") as file:
    lines = file.readlines()

def multiply(list):
    product = 1

    for num in list:
        product *= num
    
    return product

for i, line in enumerate(lines):
    for j, char in enumerate(line):                    
        if char.isdigit():
            numAsStr += char
            rowModifier = -2

            for k in range(9):
                if k % 3 == 0:
                    rowModifier += 1
                try:
                    surroundingChar = lines[abs(i + rowModifier)][abs(j + (k % 3) - 1)]
                    if surroundingChar == '*':
                        gearIndex = (abs(i + rowModifier), abs(j + (k % 3) - 1))
                        numIsAdjacent = True
                except IndexError:
                    continue 
        else:
            if numIsAdjacent:
                gearPairs.setdefault(gearIndex, [])
                gearPairs[gearIndex].append(int(numAsStr))
                numIsAdjacent = False

            numAsStr = ""

for value in gearPairs.values():
    if len(value) > 1:
        totalSum += multiply(value)

print(totalSum)
