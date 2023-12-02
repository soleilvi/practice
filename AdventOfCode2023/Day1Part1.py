numsInStr = []
totalSum = 0

with open("AdventOfCode2023/files/Day1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    for char in line:
        if char.isdigit():
            numsInStr.append(char)
    totalSum += int(numsInStr[0] + numsInStr[-1])
    numsInStr.clear()

print(totalSum)