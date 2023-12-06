# # 거리두기 확인하기 Lv2
'''
참고용 풀이)
나오는 경우의 수 대로 조건
'''
def solution(places):
    def check(place):
        for irow,row in enumerate(place):
            for icol,cell in enumerate(row):
                if place[irow][icol] != 'P':
                    continue
                if irow != 4 and place[irow+1][icol] == 'P':
                    return 0
                if icol !=4 and place[irow][icol+1] == 'P':
                    return 0
                if irow < 3 and place[irow+2][icol] == 'P' and place[irow+1][icol] != 'X':
                    return 0
                if icol < 3 and place[irow][icol+2] == 'P' and place[irow][icol+1] != 'X':
                    return 0
                if irow != 4 and icol != 4 and place[irow+1][icol+1] == 'P' and (place[irow+1][icol] != 'X' or place[irow][icol+1] != 'X'):
                    return 0
                if irow != 4 and icol != 0 and place[irow+1][icol-1] == 'P' and (place[irow+1][icol] != 'X' or place[irow][icol-1] != 'X'):
                    return 0
        return 1
    answer = []
    for place in places:
        answer.append(check(place))
    return answer


'''
내 풀이)
그래프로 접근하는 방법
'''
# def solution(places):
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#     answer = []
#     for place in places:
#         pLocation = []
#         visited = list([0] * 5 for _ in range(5))
#         flag = False
#         for i in range(5):
#             for j in range(5):
#                 if place[i][j] == 'P':
#                     pLocation.append((i,j))
#         for i in pLocation:
#             x,y = i
#             visited[x][y] = 1
#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if nx<0 or nx>=5 or ny<0 or ny>=5:
#                     continue
#                 else:
#                     if place[nx][ny] == 'P':
#                         visited[nx][ny] = 1
#                         flag = True
#                         break
#                     elif place[nx][ny] == 'O':
#                         for q in range(4):
#                             nnx = nx + dx[q]
#                             nny = ny + dy[q]
#                             if nnx<0 or nnx>=5 or nny<0 or nny>=5:
#                                 continue
#                             else:
#                                 if place[nnx][nny] == 'P' and not visited[nnx][nny]:
#                                     flag = True
#                                     break
#                         if flag:
#                             break
#             if flag:
#                 answer.append(0)
#                 break
#         else:
#             if flag:
#                 continue
#             else:
#                 answer.append(1)

                    
#     return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))