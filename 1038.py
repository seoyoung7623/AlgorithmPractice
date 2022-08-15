#1038 감소하는 수
#각자리가 중복되지않으므로 조합을 이용해서 문제를 푼다.

# num = int(input())
# list = [0,1,2,3,4,5,6,7,8,9]

# for i in range(10000):
#     for j in range(10):
#         if ((i%(10**(j+1)))//(10**j)) < ((i%(10**(j+2)))//(10**(j+1))):
#             list.append(i)
#         else:
#             break
# print(list)

from itertools import combinations


num = int(input())
list_ = []
for i in range(1,11):
    for comb in combinations(range(0,10),i):
        comb = list(comb)
        comb.sort(reverse=True)
        list_.append(int("".join(map(str,comb))))
list_.sort() 

try:
    print(list_[num])
except:
    print((-1))