import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self,key,data = None):
        self.key = key
        self.data = data
        self.n = 0
        self.children = {}

    def finalize(self):
        self.n = 1 if self.data is not None else 0
        for char, node in self.children.items():
            self.n += node.finalize()
        return self.n
    
class Trie:
    def __init__(self):
        self.head = Node(None)

    # 단어입력
    def insert(self,string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def finalize(self):
        self.head.finalize()

    # 단어찾기
    def search(self, string):
        depth = 0
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                depth += 1
                
                if curr_node.n ==1:
                    break
                
        return depth

def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    trie.finalize()
    return sum(trie.search(word) for word in words)
print(solution(["go","gone","guild"]))
            






    