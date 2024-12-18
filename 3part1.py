total = 0
instruction_step = 0
param_one = ""
param_two = ""
start_param_two = False
mult = "mul("

def restart():
    global instruction_step, param_one, param_two, start_param_two
    instruction_step = 0
    param_one = ""
    param_two = ""
    start_param_two = False

with open("Inputs\Day3Input.txt") as input:
    while True:
        c = input.read(1)

        #EOF
        if not c:
            break
        
        #Check character
        if instruction_step < 4 and c == mult[instruction_step]:
            instruction_step += 1
            continue
        
        if start_param_two:
            if len(param_two) < 3 and c.isnumeric():
                param_two += c 
                continue
            elif c == ")" and len(param_two) != 0: #If c == ")" and param2 is not null
                conta = int(param_one) * int(param_two)
                print(param_one + "*" + param_two)
                total += int(param_one) * int(param_two)
        elif instruction_step > 3:
            #If c is a number for param 1
            if len(param_one) < 3 and c.isnumeric() and start_param_two == False:
                param_one += c 
                continue
            elif c == "," and len(param_one) != 0: #If c == "," and param1 is not null
                start_param_two = True
                continue
        
        
        restart()
        if c == "m":
            instruction_step += 1

print(total)