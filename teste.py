import re
input = open("Inputs\Day3Input.txt", "r")
input = input.read()

total_sum = 0

pattern = "mul\(\d{1,3}\,\d{1,3}\)"

x = re.findall(pattern, input)

for command in x:
    mult = int(command[4:command.index(",")]) * int(command[command.index(",") + 1:command.index(")")])
    print(command[4:command.index(",")] + "*" + command[command.index(",") + 1:command.index(")")])
    total_sum += mult

print(total_sum)