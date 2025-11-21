N = int(input())
k = int(input())
left = 1
right = k
answer = 0

while left <= right:
    mid = left + (right - left) // 2

    cnt = 0
    for i in range(1,N+1):
        m = min(N,mid//i)
        if m == 0:
            break
        else:
            cnt += m
    #print(cnt)
    
    if cnt >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
    #print(left,right)


print(answer)