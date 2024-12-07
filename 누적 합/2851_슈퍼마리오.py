# 2851 슈퍼마리오 B1
'''
조건: 최대한 100에 가깝게
1. 처음에 무조건 먹어야함 안먹으면 0 점
'''
prefix_sum = float('inf')
arr = []
num = 0
for i in range(10):
    num += int(input())
    arr.append(num)

for i in range(10):
    if prefix_sum < abs(100 - arr[i]):
        print(arr[i-1])
        break
    prefix_sum = abs(100-arr[i])
else:
    print(arr[-1])



