# 15684 사다리 조작  G3
'''
백트래킹 2중 반복문 범위 주의
pypy3으로 제출해야 시간초과안남...
내 코드는 사다리를 추가할때 같은행에서 이전열만 확인함! 설치전에 그 다음에 값이 있다면 설치 불가함.
'''
import sys
input = sys.stdin.readline
N,M,H = map(int,input().split())
visited = [[False] * N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    visited[a-1][b-1] = True
answer = 4
def checking(visited):
    for i in range(N-1):
        start = i
        for j in range(H):
            if visited[j][start] == False:
                if start != 0:
                    if visited[j][start-1] == True:
                        start -= 1
            else:
                start += 1
        if start != i:
            return False
    return True

def DFS(depth,h,n,visited):
    global answer
    if depth > 3:
        return
    if checking(visited):
        answer = min(answer,depth)
    for i in range(h,H):
        for j in range(n if i == h else 0,N-1):
            if visited[i][j] ==False:
                if j != 0:
                    if visited[i][j-1] == True:
                        continue
                if j<N-2 and visited[i][j+1] == True:
                    continue
                visited[i][j] = True
                DFS(depth+1,i,j+1,visited)
                visited[i][j] = False

DFS(0,0,0,visited)
if answer == 4:
    print(-1)
else:
    print(answer)
            
# import sys
# input = sys.stdin.readline

# # 입력 처리
# N, M, H = map(int, input().split())
# visited = [[False] * (N - 1) for _ in range(H)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     visited[a - 1][b - 1] = True

# answer = 4  # 가로선 개수의 최대값 + 1

# # 모든 세로선이 자기 번호로 도착하는지 확인
# def checking():
#     for start in range(N):
#         pos = start
#         for i in range(H):
#             if pos > 0 and visited[i][pos - 1]:  # 왼쪽 가로선
#                 pos -= 1
#             elif pos < N - 1 and visited[i][pos]:  # 오른쪽 가로선
#                 pos += 1
#         if pos != start:  # 도착 위치가 시작 위치와 다르면 False
#             return False
#     return True

# # 백트래킹
# def DFS(depth, x, y):
#     global answer
#     if checking():  # 조건 만족하면 최소값 갱신
#         answer = min(answer, depth)
#         return
#     if depth == 3 or depth >= answer:  # 최대 3개까지 추가
#         return

#     for i in range(x, H):
#         for j in range(y if i == x else 0, N - 1):
#             if visited[i][j]:  # 이미 가로선이 있는 경우
#                 continue
#             if j > 0 and visited[i][j - 1]:  # 왼쪽에 가로선이 있는 경우
#                 continue
#             if j < N - 2 and visited[i][j + 1]:  # 오른쪽에 가로선이 있는 경우
#                 continue
#             # 가로선 추가
#             visited[i][j] = True
#             DFS(depth + 1, i, j + 2)  # 다음 가로선은 최소 2칸 뒤에서 탐색
#             visited[i][j] = False  # 가로선 제거
#         y = 0  # 새로운 줄에서는 처음부터 탐색

# # DFS 시작
# DFS(0, 0, 0)

# # 결과 출력
# print(answer if answer < 4 else -1)


