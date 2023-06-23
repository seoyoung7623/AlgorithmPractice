# 14888 연산자 끼워넣기 S1
# 백트래킹
# 부루트포스 알고리즘

# N = int(input())
# num_lst= list(map(int,input().split()))
# operator = list(map(int,input().split()))
# result_op = []
# result_num=[]
# num = 0
# cnt = 0

# def back():
#     if len(result_op) == N:
#         result_num.append(num)
#         num = 0
#         return
#     for i in range(N):
#         if operator[i] != 0 and op not in result_op:
#             if i == 0:
#                 num += num_list[]

#         op  = operator[i] 

import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int,input().split()))
operator = list(map(int,input().split()))

maximum = -1e9
minimum = 1e9

def back(depth,total,plus,sub,mul,div):
    global maximum,minimum
    if depth == N:
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return
    if plus: #0이 아닌 값은 모두 'True'이고 '0'은 'False'라는 일반적인 규칙
        back(depth+1,total+num_list[depth],plus-1,sub,mul,div)
    if sub:
        back(depth+1,total-num_list[depth],plus,sub-1,mul,div)
    if mul:
        back(depth+1,total*num_list[depth],plus,sub,mul-1,div)
    if div:
        back(depth+1,int(total/num_list[depth]),plus,sub,mul,div-1)


back(1,num_list[0],operator[0],operator[1],operator[2],operator[3])
print(maximum)
print(minimum)