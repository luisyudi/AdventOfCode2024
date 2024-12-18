with open("Inputs/Day4Input.txt", "r") as input_file:
    lines = [list(line.strip()) for line in input_file if line.strip()]

size_i = len(lines)
size_j = len(lines[0])

def verify(i, j):
    total = 0

    # Horizontal forward
    if j <= size_j - 4 and "".join(lines[i][j:j+4]) == "XMAS":
        total += 1
    
    # Horizontal backward
    if j >= 3 and "".join(lines[i][j-3:j+1]) == "SAMX":
        total += 1

    # Vertical upward
    if i >= 3 and "".join([lines[i-k][j] for k in range(4)]) == "XMAS":
        total += 1
    
    # Vertical downward
    if i <= size_i - 4 and "".join([lines[i+k][j] for k in range(4)]) == "XMAS":
        total += 1
    
    # Diagonal Up-Right
    if j <= size_j - 4 and i >= 3 and "".join([lines[i-k][j+k] for k in range(4)]) == "XMAS":
        total += 1

    # Diagonal Up-Left
    if j >= 3 and i >= 3 and "".join([lines[i-k][j-k] for k in range(4)]) == "XMAS":
        total += 1

    # Diagonal Down-Right
    if j <= size_j - 4 and i <= size_i - 4 and "".join([lines[i+k][j+k] for k in range(4)]) == "XMAS":
        total += 1

    # Diagonal Down-Left
    if j >= 3 and i <= size_i - 4 and "".join([lines[i+k][j-k] for k in range(4)]) == "XMAS":
        total += 1

    return total

all_xmas = 0

for i in range(size_i):
    for j in range(size_j):
        if lines[i][j] == "X":
            all_xmas += verify(i, j)

print(all_xmas)
