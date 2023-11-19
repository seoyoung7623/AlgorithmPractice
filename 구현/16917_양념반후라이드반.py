# # 양념반 후라이드반 16917
'''
min(A,2*C) * max(0,X-Y) max가 0일때 값을 이용해 사칙연산을 조건문처럼 활용가능
'''
# A,B,C,X,Y = map(int,input().split())
# if A+B<(2*C):
#     print((A*X)+(B*Y))
# else:
#     if X==Y:
#         print((2*C) * X)
#     else:
#         if X>Y:
#             gap = X-Y
#             sum = (2*C)*Y
#             if (2*C) * gap < gap* A:
#                 sum += (2*C) * gap
#             else:
#                 sum += gap * A
#         else:
#             gap = Y-X
#             sum = (2*C)*X
#             if (2*C) * gap < gap * B:
#                 sum += (2*C) * gap
#             else:
#                 sum += gap * B
#         print(sum)

A,B,C,X,Y = map(int,input().split())

if A + B < 2*C:
    print(A*X+B*Y)
else:
    print(2*C*min(X,Y) + min(A,2*C) * max(0,X-Y) + min(B, 2*C)*max(0,Y-X))