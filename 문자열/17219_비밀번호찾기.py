# 17219 비밀번호 찾기 S4
N,M = map(int,input().split())
dic = {}
for i in range(N):
    key,value = input().split()
    dic[key] = value
for i in range(M):
    site = input()
    print(dic[site])