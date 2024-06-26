class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node1=Node(3)
# node2=Node(4)
# node3=Node(5)
# node4=Node(6)
# node1.next=node2
# # node2.next=node3
# node3.next=node4
#
# current_node=node1
# while current_node:
#     print(current_node.data,"->",end=" ")
#     current_node=current_node.next
# print("null")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

    def insert_at_first_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_any_point_node(self, pos, data):
        new_node = Node(data)
        if pos == 1:
            new_node = self.head
            self.head = new_node
        current = self.head
        for i in range(pos - 2):
            if current.next is None:
                print("invalid position")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def deletion_at_first_node(self):
        current = self.head
        if current is None:
            print("empty list!!")
            return
        self.head = self.head.next
        del current

    def deletion_at_end_node(self):

        current = self.head
        if current is None:
            print("empty list!!")
            return

        # If there is only one node in the list
        if current.next is None:
            self.head = None
            return

        # Traverse to the second last node
        while current.next.next is not None:
            current = current.next

        # Remove the last node
        current.next = None

    def deletion_at_any_node(self, position):
        if not self.head:
            print("list is empty!!")
            return
        if position == 1:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 2):
                if current.next is None:
                    print("invalid position")
                    return
                current = current.next
            if current.next is None:
                print("invalid position")
                return
            current.next = current.next.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Null")


def create_linked_list():
    n = int(input("enter the number of linked list insert:  "))
    linked_list = Linked_list()
    for _ in range(n):
        data1 = int(input("enter the linked lists: "))
        linked_list.add_list(data1)
    return linked_list


linked_list1 = Linked_list()
while True:
    print(
        "1.add_the_linked_list\n2.display_linked_list\n3.insert_first_node\n4.insert_at_end_node\n5.insert_at_any_point\n6.deletion_at_first_node\n7.deletion_at_end_node\n8.deletion_at_any_node\n9.exit\n")
    ch = int(input("enter the choice: "))
    match ch:
        case 1:
            linked_list1 = create_linked_list()
        case 2:
            linked_list1.display()
        case 3:
            data = int(input("enter the data insert to the list: "))
            linked_list1.insert_at_first_node(data)
        case 4:
            data = int(input("enter the data insert to the list: "))
            linked_list1.insert_at_end_node(data)
        case 5:
            data = int(input("enter the data insert to the list: "))
            pos = int(input("enter the position insert to the list: "))
            linked_list1.insert_at_any_point_node(pos, data)
        case 6:
            linked_list1.deletion_at_first_node()
        case 7:
            linked_list1.deletion_at_end_node()
        case 8:
            pos = int(input("enter the position to delete the node"))
            linked_list1.deletion_at_any_node(pos)
        case 9:
            exit()
