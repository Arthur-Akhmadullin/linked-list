class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

n1 = Node(12)
n2 = Node(55)
n1.next = n2

class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None


    def add_in_tail(self, item):

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item


    def print_all_nodes(self):

        node = self.head
        while node != None:
            print(node.value)
            node = node.next


    def find(self, val):

        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None


    def del_alone_node(self, val):
        if self.head == None:
            return

        old = None
        node = self.head

        if node.value == val:
            self.head = self.head.next
            if node.next == None:
                self.tail = node
            return
        while node is not None:
            if node.value == val:
                if node.next == None:
                    self.tail = node
                old.next = node.next
                break
            old = node
            node = node.next

s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
s_list.print_all_nodes()
print("-----------------")


nf = s_list.find(55)
if nf is not None:
    print(nf.value)
print("-----------")

s_list.del_alone_node(128)
s_list.print_all_nodes()