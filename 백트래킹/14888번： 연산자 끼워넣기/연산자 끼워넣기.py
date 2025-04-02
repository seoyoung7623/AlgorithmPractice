#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14888                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14888                          #+#        #+#      #+#     #
#    Solved: 2025/04/01 11:17:51 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
식 계산은 앞에서 부터 진행
'''
import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int,input().split()))
op_list = list(map(int,input().split()))
max_total = -1e10
min_total = 1e10

def backtracking(depth,total,plus,sub,mul,div):
    global max_total,min_total
    if depth == N:
        max_total = max(total, max_total)
        min_total = min(total, min_total)
    if plus:
        backtracking(depth+1,total+num_list[depth],plus-1,sub,mul,div)
    if sub:
        backtracking(depth+1,total-num_list[depth],plus,sub-1,mul,div)
    if mul:
        backtracking(depth+1,total*num_list[depth],plus,sub,mul-1,div)
    if div:
        backtracking(depth+1,int(total/num_list[depth]),plus,sub,mul,div-1)

backtracking(1,num_list[0],op_list[0],op_list[1],op_list[2],op_list[3])
print(max_total)
print(min_total)