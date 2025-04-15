A,B = map(int,input().split())

arr = []
for b in range(1,B+1):
    for _ in range(b):
        arr.append(b)
sum = 0
for i in range(A-1,B):
    sum += arr[i]
print(sum)