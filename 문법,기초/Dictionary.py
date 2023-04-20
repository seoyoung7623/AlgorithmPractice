fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

# setdefault는 딕셔너리에 값이 있을 땐 해당 값을 리턴하고, 값이 없을 땐 두번째 인자로 넘겨준 값을 추가하고 추가한 값을 리턴합니다.
print(_dict.setdefault('strawberry', 0)) # 0 
print(_dict) # 'strawberry': 0  가 추가됨

print(*_dict.keys()) 
print(*_dict.values()) 
print(*_dict.items())
# 다음과 같은 keys, values, items를 통해 내부 값을 unpacking 할 수 있습니다.