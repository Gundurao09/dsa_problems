class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_duplicate_nodes(self):
        if not self.head:
            print("Empty list!")
            return

        seen = set()
        current = self.head
        prev = None

        while current:
            if current.data in seen:
                prev.next = current.next  # Skip the current node
            else:
                seen.add(current.data)
                prev = current  # Update prev to current
            current = current.next  # Move to the next node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("none")


obj = Linked_list()
while True:
    print("1.add_node\n2.display\n3.delete_duplicate_node\n4.exit")
    ch = int(input("enter the choice"))
    match ch:
        case 1:
            n = int(input("enter the no of node to insert:"))
            for _ in range(n):
                data = int(input("enter the Node: "))
                obj.add_list(data)
        case 2:
            obj.display()
        case 3:
            obj.delete_duplicate_nodes()
        case 4:
            exit()

