N, X = map(int,input().split())
arr = list(map(int,input().split()))
answer = []

prefix_sum = [0] * (N+1)

for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

for i in range(X,N+1):
    total = prefix_sum[i] - prefix_sum[i-X]
    answer.append(total)
number = max(answer)
if number != 0:
    print(number)
    print(answer.count(number))
else:
    print('SAD')
