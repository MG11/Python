# Linked list

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linked_list(Node):

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
            my_node = Node(data, self.head)
            self.head = my_node

    def printlinkedlist(self):
        itr = self.head
        while itr:
            print(str(itr.data) + "-->", end = " ")
            itr = itr.next
        print("\n")

    def reverse_a_linked_list(self):
        current = self.head
        if not current:
            print("empty linked list")
            return
        prev = None
        while current.next:
            self.head = current.next
            current.next = prev
            prev = current
            current = self.head

        self.head = current
        current.next = prev

    def reverse_using_recursion_helper(self, n : Node):
        if n.next is None:
            self.head = n
            return
        self.reverse_using_recursion_helper(n.next)
        n.next.next = n
        n.next = None
        return

    def reverse_using_recursion(self):
        return self.reverse_using_recursion_helper(self.head)


if __name__ == "__main__":

    l = linked_list()
    l.insert_at_beginning(5)
    l.insert_at_beginning(10)
    l.insert_at_beginning(20)
    l.printlinkedlist()
    l.reverse_using_recursion()
    l.printlinkedlist()

