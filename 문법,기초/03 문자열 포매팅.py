#문자열 포매팅 = 문자를 이쁘게 만드는 방법
# 1. format함수를 이용한 방법
# 2. %와 서식기호를 이용한 방법
# 3. f-string을 이용한 방법

# 1. format 함수
a = 2
b = 3

s = "구구단 {0} x {1} = {2}".format(a,b,a*b)
print(s)

s9 = "this is {0:-<10} | done {1:<5} |".format("left","a")
print(s9)

s10 = "this is {0:>10} | done {1:>5} |".format("right","b")
print(s10)

s11 = "this is {0:^10} | done {1:^5} |".format("center","c")
print(s11)

for a in range(2,4):
    for b in range(1,10):
        print('{0} X {1} = {2:2}'.format(a,b,a*b))

# 2. % 기호
names = ['kim','park','lee']
for name in names:
    print('my name is %s' %name)

money = 10000
s2 = 'give me %d won' %money
print(s2)

d = 3.141592
print('value %f' %d)


# 3. f문자열
c = 'coffee'
n = 5
result =f'저는 {c:<10}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result)

#딕셔너리
me = {'name': 'seoyoung','gender': 'man','age': 100}
result = f'my name {me["name"]}, gender {me["gender"]}, age {me["age"]}'
print(result)