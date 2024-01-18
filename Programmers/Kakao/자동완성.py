# def solution(words):
#     answer = [0] * len(words)
#     for i in range(len(words)):
#         for j in range(len(words)):
#             if i == j:
#                 continue
#             spil = 0
#             while True:
#                 if len(words[i])<= spil or len(words[j])<= spil or words[i][spil] != words[j][spil]:
#                     answer[j] = max(spil,answer[j])
#                     break
#                 spil += 1
#     for i in range(len(words)):
#         if len(words[i]) != answer[i]:
#             answer[i] += 1
#     return sum(answer)
# print(solution(["go","gone","guild"]))

## 트라이 이용

import sys
sys.setrecursionlimit(10**9)

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data # data - 문자열의 종료를 알리는 flag. ( True/False로도 구현할 수 있지만, 돌아가는 일이 없게 하기위해 전체 문자열을 저장)
        self.n = 0 # 단어 체크
        self.children = {}
    
    def finalize(self):
        self.n = 1 if self.data is not None else 0 # 1이면 끝났음
        for char, node in self.children.items(): # items함수는 딕셔너리의 (key,value),(key,value)를 전달해줌 꼬리의 꼬리를 뭄
            self.n += node.finalize() # 재귀함수
            # 다음 노드의 data값이 마지막값이면 그 앞값에 +1이 됨 그러니까 이전부터 나온 횟수 계산 DFS
        return self.n
        
class Trie(object): # 상속: 부모의 변수 사용가능
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char) # {"g":Node("g")g가 헤더,}
            curr_node = curr_node.children[char]
        
        curr_node.data = string
    
    def finalize(self):
        self.head.finalize()
        
    def search(self, string):
        depth = 0
        curr_node = self.head
        
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                depth += 1
                
                if curr_node.n == 1: #1번씩만 나오기 시작하면 멈춤
                    break
        
        return depth
            
def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    trie.finalize()
    
    return sum(trie.search(word) for word in words)
print(solution(["go","gone","guild"]))