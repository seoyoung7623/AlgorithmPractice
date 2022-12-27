#물병 1052
#그리디알고리즘 / 수학 / 비트마스킹

# N, K = map(int,input().split())
# sum = 0
# i = 0

# while N > K * (2**i):
#     cnt = 0
#     if (N // (K * (2**i))) % 2 != 0: #홀수인경우
#         if N % (K * (2**i)) != 0: #나머지가 있는경우
#             cnt += K * (2**i) - (N % (K * (2**i)))
#         else:
#             cnt += K * (2**i)
#     else: #짝수인경우
#         if N % (K * (2**i)) != 0: #나머지가 있는경우
#             cnt += K * (2**i) - (N % (K * (2**i))) + K * (2**i)
#         else:
#             cnt += 0
#     N += cnt
#     sum += cnt
#     i += 1

# # for i in range(0,K): # 2**i
# #     cnt = 0
# #     if (N // (K * (2**i))) % 2 != 0: #홀수인경우
# #         if N % (K * (2**i)) != 0: #나머지가 있는경우
# #             cnt += K * (2**i) - (N % (K * (2**i)))
# #         else:
# #             cnt += K * (2**i)
# #     else: #짝수인경우
# #         if N % (K * (2**i)) != 0: #나머지가 있는경우
# #             cnt += K * (2**i) - (N % (K * (2**i))) + K * (2**i)
# #         else:
# #             cnt += 0
# #     N += cnt
# #     sum += cnt

# print(sum)


n, k = map(int, input().split())

count = 0

while bin(n).count('1') > k:
    n = n+1
    count = count +1

print(count)

