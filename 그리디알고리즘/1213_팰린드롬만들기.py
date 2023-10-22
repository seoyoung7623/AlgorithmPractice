#1213 팰린드롬 만들기
# 그리디 알고리즘 구현 문자열

str = list(input())
strList = []
oddcnt = 0
strSet = list(set(str)) #집합으로 바꾸어 각 문자 집합 확인
center = ""

for i in strSet:
    if str.count(i)%2 !=0: #홀수발견
        center += i
        oddcnt +=1
        str.remove(i) #remove는 가장 먼저 발견한 것을 삭제한다.
        if oddcnt>=2:
            break

if oddcnt>=2:
    print("I'm Sorry Hansoo")
else:
    str.sort() 
    res =""
    for i in range(0,len(str),2): #제일 중요(짝수개 이므로)
        res += str[i]
    print(res + center + res[::-1])
    

# print(str)
# print(center)
        

# for i in str:
#     print(str.count(i))
#     if str.count(i)%2 == 0:
#         strList.append(i)
#     else:
#         oddcnt +=1
#     if oddcnt >= 2:
#         print("I'm Sorry Hansoo")
#         break
