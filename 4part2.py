with open("Inputs/Day4Input.txt", "r") as input_file:
    lines = [list(line.strip()) for line in input_file if line.strip()]

size_i = len(lines)
size_j = len(lines[0])

def verify(i, j):
    upleft = ""
    upright = ""

    #Up-Left
    if lines[i-1][j-1] == "M":
        upleft = "M"
    elif lines[i-1][j-1] == "S":
        upleft = "S"
    else:
        return 0

    #Up-Right
    if lines[i-1][j+1] == "M":
        upright = "M"
    elif lines[i-1][j+1] == "S":
        upright = "S"
    else:
        return 0

    # Down-Left
    downleft = lines[i+1][j-1]
    if downleft == "M" and upright == "M":
        return 0
    elif downleft == "S" and upright == "S":
        return 0
    elif downleft != "M" and downleft != "S":
        return 0
        
    # Down-Right
    downright = lines[i+1][j+1]
    if downright == "M" and upleft == "M":
        return 0
    elif downright == "S" and upleft == "S":
        return 0
    elif downright != "M" and downright != "S":
        return 0
        
    return 1

all_xmas = 0

for i in range(1, size_i - 1):
    for j in range(1, size_j - 1):
        if lines[i][j] == "A":
            all_xmas += verify(i, j)
print(all_xmas)
