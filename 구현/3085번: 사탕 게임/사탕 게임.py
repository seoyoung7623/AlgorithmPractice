#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3085                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3085                           #+#        #+#      #+#     #
#    Solved: 2025/04/07 09:36:15 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
행또는 열의 최대 길이
같은 문자열의 최대 길이
모든 칸에서 위아래 왼 오 한번씩 바꾸고 바뀐수의 최대 값을 넣기
자리 원상복구 핵심!!
count_max_candies
근데 하나의 칸에서 중복되는 수가 생김
처음부터 오 아래만 판단 하자
'''
import copy

N = int(input())
grid = [list(input()) for _ in range(N)]

max_candies = 1

# 모두 검사
def count_max_candies(new_grid,n):
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(1,n): # 해당 행까지만 검사
            if new_grid[i][j] == new_grid[i][j-1]:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 1
        count = 1
        for j in range(1,n): #해당 열까지만 검사
            if new_grid[j][i] == new_grid[j-1][i]:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 1
    return max_count


# 사탕 자리 변경
for i in range(N):
    for j in range(N):
        for dx,dy in [(0,1),(1,0)]:
            nx = dx + i
            ny = dy + j
            if 0<=nx<N and 0<=ny<N:
                grid[i][j],grid[nx][ny] = grid[nx][ny],grid[i][j] # 자리 변경
                max_candies = max(count_max_candies(grid,N),max_candies)
                grid[i][j],grid[nx][ny] = grid[nx][ny],grid[i][j] # 원상 복구


print(max_candies)