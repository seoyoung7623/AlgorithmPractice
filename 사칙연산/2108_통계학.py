# 2108 통계학 S3
N = int(input())
result = []
dic = dict()
for i in range(N):
    num = int(input())
    result.append(num)
result.sort()
print(round(sum(result)/len(result)))
print(result[N//2])
for i in result:
    if i in dic:
        dic[i] += 1   
    else:
        dic[i] = 1
mx = max(dic.values())
mx_list = []
for i in dic:
    if mx == dic[i]:
        mx_list.append(i)
if len(mx_list) > 1:
    print(mx_list[1])
else:
    print(mx_list[0])
print(result[-1]-result[0])

