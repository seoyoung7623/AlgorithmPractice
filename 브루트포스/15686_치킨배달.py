# 15686 치킨 배달 G5
from itertools import combinations
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
house = []
chicken = []
result = 999999

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

for chi in combinations(chicken,M):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(M): # 치킨 조합
            chi_len = min(chi_len,abs(chi[j][0]-h[0])+abs(chi[j][1]-h[1]))
        temp += chi_len
    result = min(result,temp)
print(result)
        