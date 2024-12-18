import math
input = open("Inputs\Day2Input.txt", "r")

safe_count = 0

def checkSafe(diff):
    for i in range(len(diff) - 1):
        if abs(diff[i]) > 3 or diff == 0:
            return i
        if diff[i]
        
for line in input:
    current_line = line.strip()
    isAsc = -1

    for i in range(len(current_line) - 1):
        diff = []
        v = int(current_line[i]) - int(current_line[i+1])   
        diff.append(v)
        checkSafe(diff)