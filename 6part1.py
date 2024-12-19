with open("Inputs/Day6Input.txt", "r") as input_file:
    guard_map = [list(line.strip()) for line in input_file if line.strip()]

def next_pos(guard):
    global directions
    guard = guard[0] + directions[guard_dir][0], guard[1] + directions[guard_dir][1]
    if guard[0] == map_size[0] or guard[1] == map_size[1] or guard[0] < 0 or guard[1] < 0:
        return False
    return True
    
map_size = [len(guard_map), len(guard_map[0])]
guard_symbol = ["^", ">", "v", "<"]
guard = [-1, -1]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] #Up, Right, Down, Left
guard_dir = 0
tiles = [guard]

for i in range(0, len(guard_map)):
    for j in range(0, len(guard_map[i])):
        if guard_map[i][j] in guard_symbol:
            guard = [i,j]
            break
    if(guard != [-1,-1]):
        break

while next_pos(guard, guard_dir):
    