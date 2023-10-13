# 9375 패션왕 신해빈 S3
T = int(input())

for _ in range(T):
    dic = dict()
    N = int(input())
    for i in range(N):
        value,key = input().split()
        if key not in dic: # 키 값이 존재하는지 여부 체크
            dic[key] = [value]
        else:
            dic[key].append(value)
    cnt = 1
    for i in dic.values():
        cnt *= (len(i)+1) # 착용해도 되고 안해도 되기때문에!
    print(cnt-1)