# 1945 간단한 소인수분해
T = int(input())

div = [2,3,5,7,11]

for test_case in range(1,T+1):
    N = int(input())
    cnt = [0]*5
    for i in range(5):
        while N % div[i] == 0:
            cnt[i] +=1
            N //= div[i]
    print(f'#{test_case}',*cnt)
        