#1929 약수구하기
# 약수는 대칭구조를 이루기때문에 구하려는 수의 제곱근만 약수를 구하면된다!
# ex) 12의 약수 1*12,2*6,3*4
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
n1,n2 = map(int,input().split())

for i in range(n1,n2+1):
    if i ==1: #1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1): # 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 해당 약수를 포함하는 수를 모두 제거할 수 있다
        if i%j == 0: #약수가 존재하므로 소수가 아님 약수가 존재하는 것들의 제곱근을 구해서 제거해주는 방식
            break
    else:
        print(i)




#처음코드
# for i in range(n1,n2+1):
#     cnt = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             cnt +=1
#             if cnt > 2:
#                 break
#     if i >1 and cnt<=2:
#         print(i)

#시간초 측정
# import time  
# start = time.time()      
# print("time :", time.time() - start)

# for i in range(n1,n2+1):
#     if i % 2 == 0:
#         continue
#     elif i % 3 == 0:
#         continue
#     elif i % 5 == 0:
#         continue
#     elif i % 7 == 0:
#         continue

