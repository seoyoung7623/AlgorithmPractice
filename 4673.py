li = list(range(10000))
for n in range(9980):
    s = n + (n//1000)+((n%1000)//100)+((n%100)//10) +(n%10)
    if s in li:
        del li[li.index(s)]
for i in li:
    print(i)
