#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1717                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1717                           #+#        #+#      #+#     #
#    Solved: 2025/03/25 09:49:27 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
set()함수에 내부 원소찾는법 O(1)
메모리 초과ㅠ
'''
# import sys
# input = sys.stdin.readline

# N,M = map(int,input().split())
# for test_case in range(M):
#     x,a,b = map(int,input().split())
#     set_lst = [{i} for i in range(N+1)]
#     if x == 0:
#         box = set()
#         for i in range(len(set_lst)-1,-1,-1):
#             if a in set_lst[i] or b in set_lst[i]:
#                 box |= set_lst[i]
#                 set_lst.remove(set_lst[i])
#         if box:
#             set_lst.append(box)
#     elif x == 1:
#         for i in range(len(set_lst)):
#             if a in set_lst[i] and b in set_lst[i]:
#                 print('YES')
#                 break
#         else:
#             print('NO')
    
'''
아 union-find
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
parent = [i for i in range(N+1)]

def union(a,b):
    a = find(a) # 부모값
    b = find(b) # 부모값
    if a != b:
        parent[b] = a # 부모값으로 갱신

# 주의!
def find(x):
    if parent[x] != x: 
        parent[x] = find(parent[x])
    return parent[x] # 부모 루트값

for test_case in range(M):
    op,a,b = map(int,input().split())
    if op == 0:
        union(a,b)
    elif op == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')