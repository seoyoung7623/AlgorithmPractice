# 1026 보물
# num = int(input())

# l1 = list(map(int,input().split()))
# l2 = list(map(int,input().split()))

# sum=0
# l1.sort()
# l2.sort()
# l2.reverse()
# for i in range(num):
#     sum += (l1[i] * l2[i])
# print(sum)

num = int(input())

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
sum = 0

for i in range(num):
    sum += min(l1) * max(l2)
    l1.remove(min(l1))
    l2.remove(max(l2))
print(sum)