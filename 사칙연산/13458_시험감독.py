#13458 시험 감독 B2
N = int(input())
mem = list(map(int,input().split()))
B,C = map(int,input().split())
sum = 0

for i in range(N):
    mem[i] = mem[i] - B
    sum += 1
    if mem[i] > 0: # 이 조건 빠져서 틀림!!
        if mem[i] % C == 0:
            sum += mem[i]// C
        else:
            sum += (mem[i]// C) + 1
print(sum)