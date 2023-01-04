#1931 회의실 배정
N = int(input())

room = [list(map(int,input().split())) for _ in range(N)]
room.sort(key=lambda x:(x[1],x[0]))

end = room[0][1]
cnt = 1

for i in range(1,N):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)