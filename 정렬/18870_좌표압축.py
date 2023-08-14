# 18870 좌표 압축
N = int(input())
lst1 = list(map(int,input().split()))
lst2 = sorted(list(set(lst1)))

dic = {lst2[i]: i for i in range(len(lst2))} # 인덱스 딕셔너리로 저장
for i in lst1:
    print(dic[i],end=' ')