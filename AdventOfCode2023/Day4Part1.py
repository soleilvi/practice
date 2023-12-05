totalSum = 0

with open("AdventOfCode2023/files/Day4.txt", 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    winningNums = []
    myNums = set()
    isWinningNum = True
    exponent = -1
    numAsStr = ""

    line = line.replace(f"{i + 1}: ", "")
    for char in line:
        if char.isdigit():
            numAsStr += char
        elif numAsStr and (char == ' ' or char == '\n'):
            if isWinningNum:
                winningNums.append(int(numAsStr))
            else:
                myNums.add(int(numAsStr))
            numAsStr = ""
        elif char == '|':
            isWinningNum = False

    for num in winningNums:
        if num in myNums:
            exponent += 1

    totalSum += int(pow(2, exponent))

print(totalSum)