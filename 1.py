import math

input = open("Inputs\Day1Input.txt", "r")

list1 = []
list2 = []
total = 0

for line in input:
    current_line = line.strip().split()
    list1.append(int(current_line[0]))
    list2.append(int(current_line[1]))

list1.sort()
list2.sort()

#Part 1
for i in range(len(list1)):
    total += math.fabs(int(list1[i]) - int(list2[i]))

print(total)   


similarity_score = 0
#Part 2
for i in range(len(list1)):
    similarity_score += list1[i] * list2.count(list1[i])

print(similarity_score)