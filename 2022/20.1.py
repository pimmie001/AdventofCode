import re

### node class and functions
class Node:
    def __init__(self, ind, val):
        self.ind = ind
        self.val = val
        self.prev = None
        self.next = None


def move_node(node):
    # move node one to the right
    current = node
    prev_node = node.prev
    next_node = node.next
    next_next = node.next.next

    prev_node.next = next_node
    next_node.prev = prev_node

    next_node.next = current
    current.prev = next_node

    current.next = next_next
    next_next.prev = current


def move_node_left(node):
    # move node one to the left
    current = node
    prev_node = node.prev
    prev_prev = node.prev.prev
    next_node = node.next

    prev_prev.next = current
    current.prev = prev_prev

    current.next = prev_node
    prev_node.prev = current

    prev_node.next = next_node
    next_node.prev = prev_node


def print_values(node, n):
    # node = starting node, n = number of nodes
    # prints values of nodes
    A = [node.val]
    for _ in range(n-1):
        node = node.next
        A.append(node.val)
    print(A)


### reading file and setup
with open('20.txt') as fh:
    input = fh.read()

numbers = [int(x) for x in re.findall('[-0-9]+', input)]


# node 0
first_node = Node(0, numbers[0])
nodes = [first_node] # original order of nodes

# nodes 1 ... n-2
prev = first_node
for ind in range(1, len(numbers) - 1):
    node = Node(ind, numbers[ind])
    nodes.append(node)

    node.prev = prev
    prev.next = node

    prev = node

# node n-1
node = Node(len(numbers) - 1, numbers[len(numbers) - 1])
nodes.append(node)

node.prev = prev
prev.next = node
node.next = nodes[0]

nodes[0].prev = node



### switching orders
for node in nodes:
    val = node.val
    if val > 0:
        for _ in range(val):
            move_node(node)
    elif val < 0:
        for _ in range(-val):
            move_node_left(node)
    # print_values(first_node, len(nodes)) # check


### getting answer
node = first_node
while node.val != 0:
    node = node.next


total = 0
for i in range(1, 3001):
    node = node.next
    if i % 1000 == 0:
        total += node.val

print(total) # 5904

