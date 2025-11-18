N,M,K = map(int,input().split()) #가로,세로,크기
grid = [list(input()) for _ in range(N)]

ps = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1,N+1):
    row = grid[i-1]
    row_ps = ps[i]
    prev_row_ps = ps[i - 1]
    row_sum = 0
    for j in range(1,M+1):
        col = row[j-1]
        if (i+j) % 2 == 0:
            expect = 'B'
        else:
            expect = 'W'

        mism = 1 if col != expect else 0
        row_sum += mism

        row_ps[j] = prev_row_ps[j] + row_sum

KK = K * K
answer = float('inf')
for i in range(K, N + 1):
    cur_row = ps[i]
    prev_row = ps[i - K]
    for j in range(K, M + 1):
        # KxK 영역 (i-K+1, j-K+1) ~ (i, j)의 mismatch 개수
        cnt = cur_row[j] - prev_row[j] - cur_row[j - K] + prev_row[j - K]

        repaint = cnt if cnt < KK - cnt else KK - cnt
        if repaint < answer:
            answer = repaint

print(answer)