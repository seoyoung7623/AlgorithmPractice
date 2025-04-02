T = int(input())
for test_case in range(T):
    n = int(input())
    lst = []
    while 1:
        if n == 1:
            lst.append(1)
            break
        lst.append(n % 2)
        n //= 2

    for i in range(len(lst)):
        if lst[i] == 1:
            print(i,end=' ')
        