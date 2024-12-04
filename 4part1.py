import math

with open("Inputs/Day4Input.txt", "r") as input_file:
    lines = [list(line.strip()) for line in input_file if line.strip()]

size_i = len(lines) - 1
size_j = len(lines[0]) - 1

def verify(i, j):
    total = 0

    #Horizontal forward
    if j <= size_j - 3 and lines[i][j:j+4] == "XMAS":
        total += 1
    
    #Horizontal backward
    if j >= 3 and lines[i][j - 3:j + 1] == "SAMX":
        total += 1

    #Vertical upward
    if i >=  3 and lines[i][j] + lines[i - 1][j] + lines[i - 2][j] + lines[i - 3][j] == "XMAS":
        total += 1
    
    #Vertical downward
    if i <=  size_i - 3 and lines[i][j] + lines[i + 1][j] + lines[i + 2][j] + lines[i + 3][j] == "XMAS":
        total += 1
    
    #Diagonal Up-Right
    if j <= size_j - 3 and i >= 3 and lines[i][j] + lines[i-1][j+1] + lines[i - 2][j + 2] + lines[i-3][j+3] == "XMAS":
        total +=1

    #Diagonal Up-Left
    if j >= 3 and i >= 3 and lines[i][j] + lines[i-1][j-1] + lines[i - 2][j - 2] + lines[i-3][j-3] == "XMAS":
        total +=1

    #Diagonal Down-Right
    if j <= size_j - 3 and i <= size_i - 3 and lines[i][j] + lines[i+1][j+1] + lines[i + 2][j + 2] + lines[i+3][j+3] == "XMAS":
        total +=1

    #Diagonal Down-Left
    if j >= 3 and i <= size_i - 3 and lines[i][j] + lines[i-1][j-1] + lines[i - 2][j - 2] + lines[i-3][j-3] == "XMAS":
        total +=1

    return total

all_xmas = 0

print(size_j,"s")

for i in range(size_i):
    for j in range(size_j):
        if lines[i][j] == "X":
            all_xmas += verify(i, j)
        
print(all_xmas)