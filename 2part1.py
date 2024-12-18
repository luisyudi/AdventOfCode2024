import math
input = open("Inputs\Day2Input.txt", "r")

safe_count = 0

#Part 1
for line in input:
    current_line = line.strip().split()
    isAsc = 1
    isSafe = 1
    
    if int(current_line[0]) > int(current_line[1]):
        isAsc = 0
    
    for i in range(len(current_line) - 1):
        v = int(current_line[i]) - int(current_line[i+1])
        if v == 0 or abs(v) > 3:
            isSafe = 0
            break
        if v < 0 and isAsc == 0:
            isSafe = 0
            break
        if v > 0 and isAsc == 1:
            isSafe = 0
            break

    if isSafe:
        safe_count += 1
    
print(safe_count)