#11660 구간 합 구하기 5
'''
n,m = map(int,input().split())

numlist = [list(map(int,input().split())) for _ in range(n)]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    sum = 0

    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            sum +=numlist[i][j]
    print(sum)
'''

"""
    x1, y1, x2, y2까지 배열을 모두 다 더한 값을 돌려주면 되는데 
    좌표를 받을 때마다 계산을 하면 시간초과가 걸린다.
"""  
"""
    sum_data [ i ] [ j ] = sum_data [ i ] [ j - 1 ] + sum_data[ i - 1 ] [ j ] - sum_data[ i -1 ][ j - 1 ] + data [ i ] [ j ]
"""
import sys
input = sys.stdin.readline #()쓰고 삽질함..
n,m = map(int,input().split())

numlist = [list(map(int,input().split())) for _ in range(n)]
sumlist = [[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        sumlist[i][j] = sumlist[i][j-1] + sumlist[i-1][j] - sumlist[i-1][j-1] + numlist[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(sumlist[x2][y2] - sumlist[x1-1][y2]-sumlist[x2][y1-1]+sumlist[x1-1][y1-1])
        