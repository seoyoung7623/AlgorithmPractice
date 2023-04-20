'''
packing
매개변수 앞에 * 를 붙이면 위치인자로 보낸 모든 객체들을 하나의 객체로 관리해준다.
*: 위치인자
**: 키워드 인자 딕셔너리로 사용가능

'''

def sum_all(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result
# print(sum_all(1,2,3)) # <class 'tuple'>

# packing을 이용해서 반드시 받아야하는 매개변수와 여러개를 받을수있는 매개변수를 구분해서 작성할 수 있습니다.  
def print_family_name1(father, mother, *sibling):
      print("아버지 :", father)
      print("어머니 :", mother)
      if sibling:
           print("호적 메이트..")
           for name in sibling:
                 print(name)

# print_family_name1("홍길동", '심사임당', '김태희', '윤아')

def print_faily_name2(*parent,**sibling):
     print("아버지:",parent[0])
     print("어머니:",parent[1])
     if sibling:
          print("-남매-")
          for title,name in sibling.items():
               print('{}:{}'.format(title,name))

# print_faily_name2("윤상규","이봉선",오빠='윤종혁',동생='윤종호')

'''
unpackig
packing은 여러개의 객체를 하나의 객체로 합쳐주었습니다. unpacking은 여러개의 객체를 포함하고 있는 하나의 객체를 풀어줍니다.
함수에서 unpacking을 할때는, 매개변수에서 *을 붙이는게 아니라 인자 앞에 *을 붙여서 사용합니다.

'''

def sum(a,b,c):
     return a+b+c

numbers = [1,2,3]
# sum(numbers) 에러 발생

# print(sum(*numbers))
# print(sum(*(4,5,6)))

def start(func,*args,**kwargs):
     print("함수를 시작합니다.")
     return func(*args,**kwargs)

# start(print,'안녕하세요','파이썬 꿀잼!',sep='~')


'''알고리즘에서 사용해보자'''
# 입력받은 list에서 첫번째 마지막값을 제외하고 싶어.
list = [1,2,3,4,5,6,7]
first,*rest,last = list
print(*rest)

print(list)
print(*list) # List Unpacking 하나의 객체를 풀어준다.



# print(1 if 9 in list else 2) 조건부 표현식