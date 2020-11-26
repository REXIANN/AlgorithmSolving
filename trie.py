class Node(object):
    """
    A node that consists of a trie.
    """

    def __init__(self, key, data=None):
        self.key = key # contains one letter
        self.dat = data # contains the string only for the last letter.
        self.children = {} # contians sequence of string


class Trie(object):
    from collections import deque

    def __init__(self):
        self.head = Node(None)

    # insert a string into Trie
    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)

            current_node = current_node.children[char]
        
        current_node.data = string


    # check if the string is in Trie
    def search(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                return False
            else:
                current_node = current_node.children[char]

        if current_node.data != None:
            return True


    # find the string starts with prefix in Trie
    def find_string(self, prefix):
        current_node = self.head
        result = []
        subtrie = None

        for char in prefix:
            if char not in current_node.children:
                return None
            else:
                current_node = current_node.children[char]
                subtrie = current_node

        dq = deque(subtrie.children.values())

        while dq:
            node = dq.popleft()
            if node.data != None:
                result.append(node.data)
            
            for value in node.children.values():
                dq.append(value)

        return result