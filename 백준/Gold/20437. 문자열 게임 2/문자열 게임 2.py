import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = input().strip()
    M = int(input())
    dic = {}
    for i in range(len(N)):
        if N[i] not in dic:
            dic[N[i]] = [i]
        else:
            dic[N[i]].append(i)
    max_len = 0
    min_len = float('inf')
    answer = []
    for k in dic.keys():
        if len(dic[k]) >= M:
            for i in range(len(dic[k])-M+1):
                answer.append(dic[k][i+M-1] - dic[k][i] + 1)
    if answer:
        print(min(answer),max(answer))
    else:
        print(-1)



    

