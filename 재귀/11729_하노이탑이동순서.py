# 11729 하노이 탑 이동순서 S1
# 재귀
N = int(input())
cnt = 0
result = []

def hanoi(N,start,end,via):
    global cnt
    if N == 1:
        cnt+=1
        result.append((start,end))
    else:
        hanoi(N-1,start,via,end)
        cnt+=1
        result.append((start,end))
        hanoi(N-1,via,end,start)

hanoi(N,'1','3','2')
print(cnt)
# 하오이 탑 최소 이동 횟수 = 2**N-1
for i in result:
    start,end = i
    print(start,end)

