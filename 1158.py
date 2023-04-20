#1158 요세푸스 문제
from collections import deque

N,K = map(int,input().split())

q = deque(i+1 for i in range(N))
_list = []

while q:
    for _ in range(K):
        q.rotate(-1)
    _list.append(q.pop())
# print(f"<{str(_list).strip('[]')}>")
print('<'+', '.join(map(str,_list))+'>')


#정답

'''백준 풀이'''
# import sys
# from collections import deque

# def input():
#     return sys.stdin.readline().rstrip()

# N, K = map(int, input().split())
# _list = []
# q = deque([i + 1 for i in range(N)])

# while len(q) != 0:
#     q.rotate(-K)
#     _list.append(q.pop())
#     print(q)

# print('<' + ', '.join(map(str, _list)) + '>')
#join 을 이용할때는 리스트가 문자형 리스트여야 하므로 문자열로 바꿔준다.