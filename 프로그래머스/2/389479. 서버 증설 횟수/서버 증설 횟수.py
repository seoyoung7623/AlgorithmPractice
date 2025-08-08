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