import re
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    pattern = r"^(100+1+|01)+$"
    word = input().rstrip()

    if re.fullmatch(pattern, word):
        print("YES")
    else:
        print("NO")
