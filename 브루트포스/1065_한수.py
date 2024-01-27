# 1065 한수 <브루트포스>
N = int(input())
cnt = 0

for i in range(1,N+1):
    if i <100:
        cnt += 1
    else:
        lst=list(map(int,str(i))) 
        if lst[1] - lst[0] == lst[2] - lst[1]:
            cnt += 1
print(cnt)