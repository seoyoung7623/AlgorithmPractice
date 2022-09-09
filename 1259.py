#팰린드롬수
# while 1:
#     ck = False
#     numlist = list(input())
#     if len(numlist) == 1:
#         if numlist[0] == '0':
#             break
#         print("yes")
#     else:
#         for i in range(0,len(numlist)//2):
#             if numlist[i] == numlist[len(numlist)-(i+1)]:
#                 ck = True
#             else:
#                 ck = False
#                 print("no")
#                 break
#         if ck == True:
#             print("yes")

#다른 풀이
#문자열 슬라이싱 [start:stop:step] = step부분이 음수이면 뒤집음
while True:
    n = input()

    if n =='0':
        break
    if n == n[::-1]: #문자열을 뒤집음!
        print("yes")
    else:
        print("no")