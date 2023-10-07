# 1149 RGB거리 
N = int(input())
table = [list(map(int,input().split()) ) for _ in range(N)]
for i in range(1,N):
    for j in range(3):
        if j == 0:
            table[i][j] = table[i][j] + min(table[i-1][1],table[i-1][2])
        elif j == 1:
            table[i][j] = table[i][j] + min(table[i-1][0],table[i-1][2])
        else:
            table[i][j] = table[i][j] + min(table[i-1][0],table[i-1][1])
print(min(table[-1]))