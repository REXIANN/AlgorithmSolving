class Node(object):
    def __init__(self, key, length):
        self.key = key
        self.length = length
        self.children = {}
        
        
class Trie(object):
    def __init__(self):
        self.head = Node(None, None)

        
    def insert(self, string):
        current_node = self.head
        length = len(string)
        for idx, char in enumerate(string):
            if char not in current_node.children:
                current_node.children[char] = Node(char, length - idx - 1)
            current_node = current_node.children[char]

    
    def str_count(self, string, count):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                return 0
            else:
                current_node = current_node.children[char]
        
        for key in current_node.children.keys():
            node = current_node.children[key]
            print('count', count, 'node_length', node.length)
        return 1

    
def solution(words, queries):
    answer = []
    t = Trie()
    tr = Trie()
    for word in words:
        t.insert(word)
        tr.insert(word[::-1])   
    
    for query in queries:
        if query[0] == '?':
            string, count = query[::-1].replace('?', ''), query.count('?')
            value = tr.str_count(string, count)
        else:
            string, count = query.replace('?', ''), query.count('?')
            value = t.str_count(string, count) 
        print(string, count)   
        answer.append(value)
        
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
