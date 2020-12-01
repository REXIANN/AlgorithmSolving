class Node(object):
    """
    A node that consists of a linked list.
    """ 
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None # first Node's head is always None
        self.size = 0 # size of nodes

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def printall(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            if current_node.next:
                print('> ', end='')
            current_node = current_node.next
        print()

    

