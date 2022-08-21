#2751 수정렬하기2
# 반복문내에서 int(input())을 사용하면 시간이 오래걸림!

import sys

num = int(input())
numlist = []

for i in range(num):
    numlist.append(int(sys.stdin.readline()))
numlist.sort()
for i in numlist:
    print(i)