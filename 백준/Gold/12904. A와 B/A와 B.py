S = input()
T = input()
answer = 0

while len(T)>= len(S):
    if T == S:
        answer = 1
        break
    if T[-1] == 'A':
        T = T[0:-1]
    elif T[-1] == 'B':
        T = T[0:-1]
        T = T[::-1]

print(answer)