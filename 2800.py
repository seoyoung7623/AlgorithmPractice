# 2800 괄호 제거 
# 미해결

ex = list(input())
st = []
ex2 = ex.copy()

for i in range(len(ex)):
    # st.append(0)
    if ex[i] == '(':
        st.append(i)
    elif ex[i] == ')':
        ex2.pop(i)
        ex2.pop(st.pop())
        print(ex2)