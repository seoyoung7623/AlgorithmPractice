# S1 https://www.acmicpc.net/problem/1992
'''
⭐️ 다시 풀기 

✅ 4등분 그리드를 나누는 방법: 시작점(x,y)를 받고 길이만큼 늘린다.
ex) 8길이 인경우 8의절반 4를 half로 저장한다. x,y / x,y+ha;f / x+half,y
/ x+half,y+half 4의 시작점에서 half 길이 만큼 반복한다.

✅ 현 문제 재귀 접근방법
시작점값을 저장하고 다른 문제를 발견했을때 재귀를 실행한다. 재귀는 return을 통해서 빠져나오는데
길이가 8인 경우 (0,0), (0,1)이 다를수있는데 길이를 8에서부터 1칸차이를 판단할때까지 8의 길이를 half하게 된다.
'''
import sys
input = sys.stdin.readline
N = int(input())
grid = [list(input()) for _ in range(N)]

def compose(x,y,length):
    first = grid[x][y]
    half = length // 2
    for i in range(x,x+length):
        for j in range(y,y+length):
            if grid[i][j] != first:
                return f"({compose(x,y,half)}{compose(x,y+half,half)}{compose(x+half,y,half)}{compose(x+half,y+half,half)})"
    return first

print(compose(0,0,N))

