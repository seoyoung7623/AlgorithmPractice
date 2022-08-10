


num = int(input())
cnt = 1

for i in range(0,7):
    if num == num % (2**(6-i)):
        continue
    else:
        num = num % (2**(6-i))
        if num == 0:
            break
        elif 32<=num<64:
            cnt +=1
            continue
        elif 16<=num<32:
            cnt +=1
            continue
        elif 8<=num<16:
            cnt +=1
            continue
        elif 4<=num<8:
            cnt +=1
            continue
        elif 2<=num<4:
            cnt +=1
            continue
        elif num ==1:
            cnt +=1
            break
print(cnt)

# if list[5]<=num<=list[6]:
#     for i in range(5):
#         if num in list:
#            cnt += 1 
#            break
#         else:
#             num = num % (2**(5-i))
#             cnt +=1
# print(cnt)

# elif list[4]<num<list[5]:
# elif list[3]<num<list[4]:
# elif list[2]<um<list[3]:
# elif list[1]<num<list[2]:
# elif list[0]<num<list[1]:
