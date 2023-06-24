# 1138 한줄로 서기 S2
# 구현 
import sys
input = sys.stdin.readline

N = int(input())
list = list(map(int,input().split()))
result = [0]*N

for i in range(N):
    t = list[i-1]
    cnt = 0
    for j in range(N):
        if cnt == t and result[j] ==0:
            result[j] = i
            break
        elif result[j] == 0:
            cnt += 1
print(*result)