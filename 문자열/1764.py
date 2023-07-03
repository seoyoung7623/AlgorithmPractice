# 1764 듣보잡 S4
'''
자료구조
문자열
정렬
해시를 사용한 집합과 맵
'''
N,M = map(int,input().split())

Nlst =set()
Mlst = set()
for i in range(N):
    d = input()
    Nlst.add(d)
for j in range(M):
    b = input()
    Mlst.add(b)
result = sorted(list(Nlst & Mlst))
print(len(result))
for i in result:
    print(i)


