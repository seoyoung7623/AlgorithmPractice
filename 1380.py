n = 1
result = []

while n:
    n = int(input())
    names = [input() for i in range(n)]
    values = []

    for i in range(2* n -1):
        a = int(input().split()[0])
        values.append(a)

    values.sort()
    for i in range(0,len(values),2):
        if i == (len(values)-1) or values[i] !=values[i+1]:
            result.append(names[values[i]-1])
            break
for i in range(len(result)):
    print(i+1,result[i])


# s = []

# while 1:
#     num = int(input())
#     if num != 0:
#         cnt = 0
#         for i in range(num):
#             name = input()
#             cnt += 1
#             s.append([name,cnt])
#         values = []
#         for i in range(1,num*2):
#             s, n = input().split()
#             values.append(int(s))
#             if values.count(i) != 2:
#                 for j in range(len(s)):
#                     if int(s[j][0]) == i:
#                         del s[j]
#     else:
#         break

# print(s)
