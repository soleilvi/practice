symbols = {'#', '=', '@', '%', '*', '$', '&', '-', '+', '/'}
numIsAdjacent = False
numAsStr = ""
totalSum = 0

with open("AdventOfCode2023/files/Day3.txt", "r") as file:
    lines = file.readlines()

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
                    if surroundingChar in symbols:
                        numIsAdjacent = True
                except IndexError:
                    continue 

        else:
            if numIsAdjacent:
                totalSum += int(numAsStr)
                numIsAdjacent = False
            numAsStr = ""
    
print(totalSum)
