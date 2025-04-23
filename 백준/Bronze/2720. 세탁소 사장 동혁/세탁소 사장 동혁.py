T = int(input())
for test_case in range(T):
    Q,D,N,P = 0,0,0,0
    money = int(input())
    Q = money // 25
    money -= 25*Q
    D = (money % 25) // 10
    money -= 10*D
    N = (money % 10) // 5
    money -= 5*N
    P = money % 5
    print(Q,D,N,P)