import sys
sys.setrecursionlimit(10000)

def draw(n, x, y, canvas):
    if n == 1:
        canvas[x][y] = '*'
        return

    height = 2**n - 1
    width = 2**(n+1) - 3

    if n % 2 == 1:
        # 정삼각형 (▲)
        for i in range(height):
            canvas[x + i][y - i] = '*'
            canvas[x + i][y + i] = '*'
        for j in range(-height+1, height):
            canvas[x + height - 1][y + j] = '*' # 가장 긴 별 길이 채우기
        # 내부 삼각형 호출
        draw(n - 1, x + height // 2, y, canvas)
    else:
        # 역삼각형 (▼)
        for i in range(height):
            canvas[x + i][y + (width//2) - i] = '*'
            canvas[x + i][y - (width//2) + i] = '*'
        for j in range(-height+1, height):
            canvas[x][y + j] = '*' # 가장 긴 별 길이 채우기
        # 내부 삼각형 호출
        draw(n - 1, x + 1, y, canvas)

def main():
    N = int(input())
    H = 2**N - 1
    W = 2**(N+1) - 3
    # 일단 밑그림 크기부터 결정
    canvas = [[' ' for _ in range(W)] for _ in range(H)]

    # 시작 위치
    if N % 2 == 1: # 홀수
        draw(N, 0, W // 2, canvas) # N번째, 세로, 가로, 캔버스
    else: # 짝수
        draw(N, 0, W // 2, canvas)

    for row in canvas:
        print(''.join(row).rstrip())

main()