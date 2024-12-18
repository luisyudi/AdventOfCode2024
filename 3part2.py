total = 0
instruction_step = 0
param_one = ""
param_two = ""
start_param_two = False
mult = "mul("

#part 2
do = True
dont_string = "don't()"
do_string = "do()"
last_instruction = ""
d_step = 0

def restart():
    global instruction_step, param_one, param_two, start_param_two
    instruction_step = 0
    param_one = ""
    param_two = ""
    start_param_two = False

def reset_d():
    global last_instruction, d_step
    d_step = 0
    last_instruction = ""

with open("Inputs\Day3Input.txt") as input:
    while True:
        c = input.read(1)

        #EOF
        if not c:
            break

        if c == dont_string[d_step]:
            last_instruction += c
            d_step += 1
            if last_instruction == dont_string:
                do = False
                reset_d()
        elif d_step < 4:
            if c == do_string[d_step]:
                last_instruction += c
                d_step += 1
                if last_instruction == do_string:
                    do = True
                    reset_d()
        else: 
            reset_d()

        
        if do:
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