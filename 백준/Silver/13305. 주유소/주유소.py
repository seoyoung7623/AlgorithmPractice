import sys
input = sys.stdin.readline
N = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))
total = 0
min_price = 1e10
for i in range(N-1):
    min_price = min(min_price,prices[i])
    total += min_price * roads[i]
print(total)