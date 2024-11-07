# 1931 회의실 배정 S1
N = int(input())
list = [list(map(int,input().split())) for _ in range(N)]
list.sort(key = lambda x:(x[1],x[0]))

end = list[0][1]
cnt = 1

for meeting in list:
    if meeting[0]>=end:
        end = meeting[1]
        cnt += 1
print(cnt)