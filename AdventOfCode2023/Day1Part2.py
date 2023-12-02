numsInStr = []
numNames= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
totalSum = 0

with open("AdventOfCode2023/files/Day1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    for i, numName in enumerate(numNames):
        line = line.replace(numName, f"{numName}{i}{numName}")
    
    for char in line:
        if char.isdigit():
            numsInStr.append(char)
            
    totalSum += int(numsInStr[0] + numsInStr[-1])
    numsInStr.clear()

print(totalSum)