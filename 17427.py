# num=int(input())
# sum =0

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         if i%j==0:
#             sum += j

# print(sum)

#시간복잡도가 O(n)인 값으로 다시
num = int(input())
sum = 0

for i in range(1, num+1):
    sum +=(num//i)*i
print(sum)