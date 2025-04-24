N = int(input())
stand = 2
for i in range(N):
    stand = stand + (2**i)
    answer = (stand)**2
print(answer)