class Node:    
    def __init__(self, value):        
        self.value = value        
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_after(self, target, element):
        new_node = Node(element)
        current = self.head
        while current is not None:
            if current.value == target:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
    
    def insert_head(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def clear(self):
        self.head = None

total = 0
read_orders = False
rules = [[] for _ in range(100)]
order = []

def check_order(new_number):
    global order
    if order == []:
        order.append(new_number)
        return True
    
    for num in order:
        for rule in rules[new_number]:
            if int(rule) == num:
                return False
    
    order.append(new_number)
    return True

def get_middle_page(order):
    size = len(order)
    print(size)
    return order[(size - 1) // 2]


with open("Inputs/Day5Input.txt", "r") as input_file:
    for line in input_file:
        if line == "\n":
            read_orders = True
            continue
        
        if read_orders:
            read_char = 0
            num = ""
            f = True
            while True:
                c = line[read_char]

                if c == "\n":
                    if check_order(int(num)) == False:
                        f = False
                    break

                read_char += 1

                if c == ",":
                    if check_order(int(num)) == False:
                        f = False
                    num = ""
                    continue
                num += c

            if f:
                total += get_middle_page(order)
            
            order = []
        else:
            param_1 = int(line[0:line.index("|")])
            param_2 = line[line.index("|") + 1:-1]
            rules[param_1].append(param_2)

print(total)