#1213 팰린드롬 만들기
# 그리디 알고리즘 구현 문자열

str = list(input())
strList = []
oddcnt = 0
strSet = list(set(str)) #집합으로 바꾸어 각 문자 집합 확인
center = ""

for i in strSet:
    if str.count(i)%2 !=0:
        center = i * str.count(i)
        oddcnt +=1
        str.remove(i)
    if oddcnt>=2:
        print("I'm Sorry Hansoo")
        break
print(str)
        

for i in str:
    print(str.count(i))
    if str.count(i)%2 == 0:
        strList.append(i)
    else:
        oddcnt +=1
    if oddcnt >= 2:
        print("I'm Sorry Hansoo")
        break
