# 달리기 경주
# def solution(players, callings):
#     for call in callings:
#         x = players.index(call)
#         players[x],players[x-1] = players[x-1],players[x]
#     return players
# 인덱스 탐색 -> 시간초과 발생

# 인덱스 탐색을 딕셔너리로 이용하는 방법

def solution(players,callings):
    answer = {player:i for i,player in enumerate(players)}
    for who in callings:
        idx = answer[who]
        answer[who] -= 1
        answer[players[idx-1]] += 1
        players[idx],players[idx-1] = players[idx-1],players[idx]
    return players