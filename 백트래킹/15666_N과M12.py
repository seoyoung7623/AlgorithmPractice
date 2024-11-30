# 문제: 백준 15666 N과 M (12) S2
'''
백트레킹
'''
N,M = map(int,input().split())
arr = list(map(int,input().split()))
answer = []
arr.sort()

def backtracking(n,lst):
    global answer
    if len(lst) == M:
        if list(lst) in answer:
            return
        answer.append(list(lst))
        print(*lst)
        return
    for i in range(n,len(arr)):
        lst.append(arr[i])
        backtracking(i,lst)
        lst.pop()
backtracking(0,[])


