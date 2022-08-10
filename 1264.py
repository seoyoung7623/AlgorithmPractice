# str = input();
# cnt = 0

# for ch in str:
#     if 'a'or'A' in ch:
#         cnt =+ 1
#     elif 'e'or 'E' in ch:
#         cnt += 1
#     elif 'i'or'I' in ch:
#         cnt += 1
#     elif 'o'or'O' in ch:
#         cnt += 1
#     elif 'u'or'U' in ch:
#         cnt += 1
# print(cnt)

#if에 in 사용가능
while 1:
    cnt = 0
    str = input()
    if str == '#':
        break
    for ch in str:
        if ch in ['a','e','i','o','u','A','E','I','O','U']:
            cnt +=1
    print(cnt)