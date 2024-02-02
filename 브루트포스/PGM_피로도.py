# # 피로도 Lv2
# 1. 순열을 이용한 모든순서 탐색
# from itertools import permutations
# def solution(k,dungeons):
#     answer = []

#     for i in permutations(dungeons,len(dungeons)):
#         total = k
#         cnt = 0
#         for dungeon in i:
#             if dungeon[0]>total:
#                 continue
#             total -= dungeon[1]
#             cnt += 1
#         answer.append(cnt)
#     return max(answer)
# print(solution(80,[[80,20],[50,40],[30,10]]))

# 2. 백트래킹을 이용한 방법
answer = 0

def backtracking(k,cnt,dungeons,visited):
    global answer
    if cnt > answer: # 큰 값으로 업데이트
        answer = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k>= dungeons[i][0]:
            visited[i] = 1
            backtracking(k-dungeons[i][1],cnt + 1, dungeons,visited)
            visited[i] = 0


def solution(k,dungeons):
    global answer
    visited = [0] * len(dungeons)
    backtracking(k,0,dungeons,visited)
    return answer
    
print(solution(80,[[80,20],[50,40],[30,10]]))



