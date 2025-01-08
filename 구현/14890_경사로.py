# # 14890 경사로 G3
# '''
# 높이차 1
# N<=10^2 L=경사로의 길이 
# 1. 올라가는 경우. 다음 경사를 만났을때 이전 경사가 L길이만큼 가능한지 확인
# 2. 내려가는 경우. 다음 경사를 만났을때 다음 경사가 L길이만큼 가능한지 확인

# '''
# N,L = map(int,input().split())
# grid = [list(map(int,input().split())) for _ in range(N)]
# answer = 0
# # 가로 길
# '''
# 시작할때 내려가는건 ok
# 끝날때 올라가는건 ok
# '''
# for i in range(N):
#     cnt = 1
#     flag = True
#     for j in range(1,N): 
#         if grid[i][j] == grid[i][j-1]:
#             cnt += 1
#             if j == N-1 and cnt<L:
#                 break
#         elif grid[i][j] == grid[i][j-1]+1:
#             if cnt < L:
#                 break
#             if not flag and cnt < L+L:
#                 break
#             cnt = 1
#             flag = True
#         elif grid[i][j] == grid[i][j-1]-1:
#             if cnt < L and j != 1:
#                 break
#             cnt = 1
#             flag = False
#         else:
#             break
#     else:
#         answer += 1

# # 세로 길
# for i in range(N):
#     cnt = 1
#     flag = True
#     for j in range(1,N):
#         if grid[j][i] == grid[j-1][i]:
#             cnt += 1
#             if j == N-1 and cnt<L:
#                 break
#         elif grid[j][i] == grid[j-1][i] + 1:
#             if cnt < L:
#                 break
#             if not flag and cnt < L+L:
#                 break
#             cnt = 1
#             flag = True
#         elif grid[j][i] == grid[j-1][i] - 1:
#             if cnt < L and j != 1:
#                 break
#             cnt = 1
#             flag = False
#         else:
#             break
#     else:
#         answer += 1

# print(answer)
'''
경사로를 메모라이즈해서 경사로를 놓을 수 없는 경우를 처리
칸이 변하면 경사로를 설치하여 일정한 값인지 확인이 가능, 경사로를 설치할수있는지 확인가능
'''
def can_place_slope(line, L):
    used = [False] * len(line)
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:  # 높이가 같은 경우
            continue
        elif line[i] == line[i - 1] + 1:  # 올라가는 경사로
            if i - L < 0 or any(used[i - L:i]): # 칸이 바뀌는경우에 used값을 체크해서 값이 일정한지 확인
                return False
            for j in range(i - L, i):
                used[j] = True
        elif line[i] == line[i - 1] - 1:  # 내려가는 경사로
            if i + L > len(line) or any(used[i:i + L]):
                return False
            for j in range(i, i + L):
                used[j] = True
        else:  # 높이 차가 1 이상인 경우
            return False
    return True

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 가로 검사
for row in grid:
    if can_place_slope(row, L):
        answer += 1

# 세로 검사
for col in zip(*grid):
    if can_place_slope(col, L):
        answer += 1

print(answer)
