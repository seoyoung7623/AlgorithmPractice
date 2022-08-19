#1874 스택 수열

cnt = int(input())
st= []
op= []
num = 1
temp = True

for i in range(cnt):
    n = int(input())
    while num <= n:
        st.append(num)
        op.append('+')
        num +=1
    if st[-1] == n:
        st.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)