# 조합문제 접근중 하나
# 비스의 1,0을 검사하여 조합을 만든다.

arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n):  # 1 << n은 2의 n제곱
    subset = []
    for j in range(n):
        if i & (1 << j):  # j번째 비트가 1인지 확인
            subset.append(arr[j])
    print(subset)
