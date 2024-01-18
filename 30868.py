# 개표
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    n = int(input())
    width = n//5
    height = n%5
    print("++++ "*width+"|"*height)