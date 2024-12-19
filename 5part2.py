total = 0
read_orders = False
rules = [[] for _ in range(100)]
order = []

class Node:    
    def __init__(self, value):        
        self.value = value        
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def get_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def insert(self, new_num):
        global rules
        current = self.head
        prev = None
        while current is not None:
            if has_rule(current.value, new_num):
                new_node = Node(new_num)
                new_node.next = current
                if prev is None:  
                    self.head = new_node
                else: 
                    prev.next = new_node
                return
            prev = current
            current = current.next
        self.insert_head(new_num) 
            
    
    def insert_head(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def clear(self):
        self.head = None


llist = LinkedList()

def check_order(new_number):
    global order
    has_order = True
    if order == []:
        order.append(new_number)
        return True
    
    for num in order:
        for rule in rules[new_number]:
            if int(rule) == num:
                has_order = False
    
    order.append(new_number)
    return has_order

def get_middle_page(order):
    size = len(order)
    return order[(size - 1) // 2]

def has_rule(value, rule):
    global rules
    for num in rules[rule]:
        if int(value) == int(num):
            return True
    return False


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
            
            if f == False:
                llist.clear()
                for num in order:
                    llist.insert(int(num))

                print(order)
                print(llist.get_list())
                print("")
                
                total += get_middle_page(llist.get_list())
            
            order = []
        else:
            param_1 = int(line[0:line.index("|")])
            param_2 = line[line.index("|") + 1:-1]
            rules[param_1].append(param_2)

print(total)