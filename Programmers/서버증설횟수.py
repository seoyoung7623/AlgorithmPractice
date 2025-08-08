'''
Lv2 그리디 문제
'''
def solution(players, m, k):
    servers = [0]*24
    cnt = 0
    for i in range(24):
        server = players[i] // m
        if server > servers[i]:
            upgrade = (server-servers[i])
            for j in range(k):
                if i+j < 24:
                     servers[i+j] += upgrade
            cnt += upgrade
    return cnt
            
print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5],3,5))