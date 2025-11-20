N = input()
if sum(map(int,N)) % 3 != 0:
    print(-1)
    exit()

N = sorted(N, reverse=True)
N = (int(''.join(N)))
if N % 30 == 0:
    print(N)
else:
    print(-1)