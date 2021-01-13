class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}