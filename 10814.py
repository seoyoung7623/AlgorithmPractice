#10814 나이순 정렬
import sys

num = int(input())
memlist = []

for i in range(num):
    memlist.append(list(sys.stdin.readline().split()))
memlist.sort(key=lambda x:int(x[0])) #sys로 받았으므로 int로 변경해줌!!
for i in memlist:
    print("{} {}".format(i[0],i[1]))