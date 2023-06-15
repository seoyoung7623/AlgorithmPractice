#14501 퇴사 S3
# N = int(input())
# arr = []

# for i in range(N):
#     T,P = map(int,input().split())
#     arr.append(T,P)

# money = [[0]*N]
# for i in range(N):
#     money[arr[i][0]+i] = arr[i][0],arr[i][1]
#     stn = max(i+arr[i][0],stn)
#     if >

# # Bottem-up방식 -> 반복문  and Top-down 재귀호출
# import sys
# N = int(input())

# schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# dp = [0 for i in range(N+1)]

# for i in range(N):
#     for j in range(i+schedule[i][0], N+1):
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]

# print(dp[-1])

# Top-down 재귀호출
# N = int(input())
# li = [list(map(int, input().split())) for _ in range(N)]
# dp = [0 for _ in range(N+1)]

# for i in range(N-1, -1, -1):
#     # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
#     if i + li[i][0] > N:
#         dp[i] = dp[i+1]
#     else:
#         # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
#         dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]]) #dp가 뒷날까지 얻은 수입

# print(dp[0])

#Bottom-up방식으로 다시 풀기
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]
# dp = [[0] *(N+1)] 이거는 [[0,0,0,0,0]] 이렇게 리스트 안에 생성 됨

for i in range(N):
    for j in range(arr[i][0]+i,N+1):
        if dp[j]< dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])