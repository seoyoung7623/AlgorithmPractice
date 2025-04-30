import sys
input = sys.stdin.readline

N = int(input())
lst = [input().rstrip() for _ in range(N)]
lst.sort(key=lambda x:-len(x))
answer = []

for i in range(len(lst)):
    for j in range(len(answer)):
        if answer[j].startswith(lst[i]):
            break
    else:
        answer.append(lst[i])

print(len(answer))