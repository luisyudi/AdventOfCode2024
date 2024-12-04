import re

input = open("Inputs\Day3Input.txt", "r")
input = input.read()

p_mul = "mul\(\d{1,3}\,\d{1,3}\)"
p_do = "do\(\)"
p_dont = "don't\(\)"

total_sum = 0
actual_index = 0
last_mul = 0
last_d = 0
execute_mul = 1

while True:
    pos = []

    last_mul = re.search(p_mul, input[actual_index])
    last_do = re.search(p_do, input[actual_index])
    last_dont = re.search(p_dont, input[actual_index])

    if last_mul != None:
        last_mul = last_mul.start()
        pos.append(last_mul)
    if last_do != None:
        last_do = last_do.start()
        pos.append(last_do)
    if last_dont != None:
        last_dont = last_dont.start()
        pos.append(last_dont)
    
    if last_mul < last_do and last_mul < last_dont and execute_mul:
        op1 = int(input[last_mul:input[last_mul].index(",")])
        op2 = int(input[input[last_mul].index(",") + 1:input[last_mul].index(")")])
        total_sum += op1 * op2
    
    if last_do < last_dont and last_do < last_mul:
        execute_mul = 1

    if last_dont < last_do and last_dont < last_mul:
        execute_mul = 0

    if pos == []:
        break

    actual_index = min(pos) + 1
    
print(total_sum)