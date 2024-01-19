# # 15654 N과M(5)
# # 지정 숫자들의 순열 사전순 중복혀용
# N,M = map(int,input().split())
# arr = list(map(int,input().split()))
# answer = []

# def backtracking(start):
#     if start == M:
#         answer.append(list(box))
#         return
#     for i in range(N):
#         if arr[i] in box: # box에 있는것을 continue한다면 정렬을 지킬수있음 / a,b의 중복을 막는 조건
#             continue
#         box.append(arr[i])
#         backtracking(start+1)
#         box.pop()
# arr.sort() #사전순
# box = []
# backtracking(0)
# for i in answer:
#     print(*i)  

# 2024.01.19에 다시 푼 풀이
n,m = map(int,input().split())
number = list(map(int,input().split()))
answer = []
number.sort()
lst = []

def backtracking(length):
    if length == m:
        answer.append(list(lst))
        return
    for i in range(n):
        if number[i] in lst:
            continue
        lst.append(number[i])
        backtracking(length+1)
        lst.pop()
backtracking(0)
for i in answer:
    print(*i)


'''
이 코드가 안되는 이유
(1,7),(1,8),(1,9),(7,8)!! (7,1)이 나와야함
따라서 start로 0부터 받아야하는데 그러면 (a,b) a,b가 중복될수있기때문에
a,b가 중복되지 않도록 하는 조건이 필요함!
'''
# n,m = map(int,input().split())
# number = list(map(int,input().split()))
# answer = []
# number.sort()

# def backtracking(start,lst):
#     if len(lst) == m:
#         answer.append(list(lst))
#         return
#     for i in range(start,n):
#         lst.append(number[i])
#         backtracking(0,lst)
#         lst.pop()

# backtracking(0,[])
# for i in answer:
#     print(*i)