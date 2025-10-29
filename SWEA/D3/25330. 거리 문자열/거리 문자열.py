T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = list(map(int,input().strip()))
    n = len(num)
    visited = [0]*n

    cnt = [0] * 10
    for d in num:
        cnt[d] += 1
    if any(c not in (0, 2) for c in cnt):
        print('no')
        continue
    
    for i in range(len(num)):
        if visited[i] == 0:
            j = i+num[i]+1
            if j < len(num) and visited[j] == 0 and num[j] == num[i]:
                visited[i+num[i]+1] = 1
                visited[i] = 1
            else:
                print('no')
                break
    else:
        print('yes')