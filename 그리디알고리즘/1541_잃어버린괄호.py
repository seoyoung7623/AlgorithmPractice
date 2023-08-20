#1541 잃어버린 괄호 S2

arr = input().split('-')
s = 0

for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -=int(j)
print(s)



# ans = input()
# ansCopy = ans[:] #Shallow copy
# op = []
# numlst = []
# ansCopy = ansCopy.replace('-','+')
# numlst = ansCopy.split('+')
# result = []
# for i in ans:
#     if i =='+':
#         op.append(i)
#     elif i == '-':
#         op.append(i)
# visited = [0]*len(op)

# def DFS(v,op,numlst):
#     visited[v] = 1
#     for i in range(len(op)):
#         if not visited[i]:
#             if op[i] =='+':
#                 numlst[i] = int(numlst[i]) + int(numlst[i+1])
#             else:
#                 numlst[i] = int(numlst[i]) - int(numlst[i+1])
#             del numlst[i+1]
#             del op[i] 
#             DFS(i,op,numlst)
#     return 
# for i in range(len(op)):
#     result.append(DFS(i,op,numlst))
    
# print(min(result))