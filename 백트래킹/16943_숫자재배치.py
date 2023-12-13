# 16943 숫자 재배치 S1
'''
순열 백트래킹
'''
A,B = input().split()
A = sorted(A)
answer = 0

def backtrack(start):
    global answer
    if start == len(A):
        if int(''.join(A)) < int(B) and A[0] != '0':
            answer = max(answer,int(''.join(A)))
        return
    for i in range(start,len(A)):
        A[start],A[i] = A[i],A[start]
        backtrack(start+1)
        A[i],A[start] = A[start],A[i]

if int(''.join(A)) > int(B):
    print(-1)
else:
    backtrack(0)
    if answer == 0:
        print(-1)
    else:
        print(answer)
