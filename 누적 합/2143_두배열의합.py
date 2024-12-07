# 2143 두 배열의 합 G3
'''
부배열의 합을 딕셔너리로 저장
'''
T = int(input())
N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))

# 딕셔너리에 저장할 N배열
arr1_dic = {}
cnt = 0

sum_arr1 = [0]
sum = 0
for i in range(N):
    sum += arr1[i]
    sum_arr1.append(sum)

sum_arr2 = [0]
sum = 0
for i in range(M):
    sum += arr2[i]
    sum_arr2.append(sum)

for i in range(N+1):
    for j in range(i):
        if sum_arr1[i]-sum_arr1[j] in arr1_dic:
            arr1_dic[sum_arr1[i]-sum_arr1[j]] += 1
        else:
            arr1_dic[sum_arr1[i]-sum_arr1[j]] = 1

for i in range(M+1):
    for j in range(i):
        if T - (sum_arr2[i]-sum_arr2[j]) in arr1_dic:
            cnt += arr1_dic[T - (sum_arr2[i]-sum_arr2[j])]
print(cnt)