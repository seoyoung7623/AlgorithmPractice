import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(input().rstrip() for _ in range(N))
answer = 0

for _ in range(M):
    word = input().strip()
    if word in lst:
        answer += 1
print(answer)
