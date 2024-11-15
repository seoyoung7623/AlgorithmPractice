# 21425 +=
'''
a+=b
b+=a
작은쪽에 큰수를 더한다.
'''
T = int(input())
for test_case in range(1, T + 1):
    A,B,N = map(int, input().split())
    sum = 0
    cnt = 0
    while True:
        if A>N:
            break
        if A>B:#B가 항상 크다
            A, B = B, A
        A += B
        cnt += 1

    print(cnt)


