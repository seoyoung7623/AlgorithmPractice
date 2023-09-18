from collections import deque

def solution(A, B):
    answer = 0
    q = deque(A)
    for i in range(0,len(A)):
        if list(q) == list(B):
            answer = i
            break
        q.rotate(1)
    else:
        answer = -1
    return answer
print(solution("apple","elppa"))