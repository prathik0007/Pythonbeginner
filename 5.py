class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


values = list(map(int, input().split()))

head = None
tail = None

# Create linked list
for value in values:
    if value == -1:
        break

    new_node = Node(value)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node


# Reverse linked list
previous = None
current = head

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

head = previous


# Print reversed linked list
current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next

print("-1")