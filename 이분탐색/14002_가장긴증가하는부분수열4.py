# G4
'''
10 20 5 6 7 30 20 50
<추적 배열> 이용 이전 인덱스를 저장
DP방식
'''
N = int(input())
arr = list(map(int,input().split()))

trace = [-1]*N
dp = [1]*N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] + 1 > dp[i]:
                trace[i] = j
                dp[i] = dp[j] + 1

max_count = max(dp)
index = dp.index(max_count)
answer = []
while index != -1:
    answer.append(arr[index])
    index = trace[index]

print(max_count)  
print(*answer[::-1])