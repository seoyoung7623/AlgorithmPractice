N = int(input())

if N == 1:
    print('*')
else:
    for i in range(N):
        if i == 0:
            print(' '*(N-1)+'*')
        elif i == N-1:
            print('*'+' '*(2*i-1)+'*')
        else:
            print(' '*(N-i-1)+'*'+' '*(2*i-1)+'*')