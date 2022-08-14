#1021 회전하는 큐 다시

n, c = map(int,input().split())
q = [i+1 for i in range(n)]
num = list(map(int,input().split()))
cnt = 0

for j in range(len(num)):
    if q[0] == num[j]:
            q.remove(num[j])
            continue
    for i in range(len(q)):
        if q[(n-1)//2] >= num[j]:
            #왼쪽이동
            if i >= len(q)-1:
                q[i] = q[0]
            else:
                q[i] = q[i+1]
        else:
            #오른쪽이동
            if i == len(q)-1:
                q[0] = q[i]
            else:
                q[i+1] = q[i]
        cnt += 1
print(cnt)

