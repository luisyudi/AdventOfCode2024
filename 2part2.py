import math
input = open("Inputs\Day2Input.txt", "r")

safe_count = 0

def test_line(line):
    asc_count = 0
    desc_count = 0
    first_asc = -1
    first_desc = -1
    list_test = []
    
    for i in range(len(line) - 1):
        v = int(line[i]) - int(line[i + 1])
        if v == 0 or abs(v) > 3: 
            list_test.append(i)
            list_test.append(i + 1)
            continue
        if v > 0:  
            desc_count += 1
            if first_desc == -1:
                first_desc = i
            if min(desc_count, asc_count) == 2:
                list_test.append(i)
                list_test.append(first_asc)
        else:  
            asc_count += 1
            if first_asc == -1:
                first_asc = i
            if min(desc_count, asc_count) == 2:
                list_test.append(i)
                list_test.append(first_desc)

    return list(dict.fromkeys(list_test))


for line in input:
    current_line = line.strip().split()
    isSafe = 0

    list_test = test_line(current_line)
    if list_test == []:
        isSafe = 1

    for i in range(len(list_test)):
        copy_list = current_line.copy()
        copy_list.pop(list_test[i])  

        if test_line(copy_list) == []:
            isSafe = 1
            break

    if isSafe:
        safe_count += 1

print(safe_count)