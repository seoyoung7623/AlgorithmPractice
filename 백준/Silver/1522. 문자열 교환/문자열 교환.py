import sys
input = sys.stdin.readline

N = input().strip()
a_cnt = N.count('a')
NN = N + N
answer = 1e3
for i in range(len(NN)-a_cnt+1):
    b_cnt = NN[i:i+a_cnt].count('b')
    answer = min(b_cnt,answer)
print(answer)

