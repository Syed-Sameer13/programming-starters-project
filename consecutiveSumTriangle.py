s=list(map(int,input().split(',')))
L=[s]

for j in range(len(s)-1):
    k=len(s)-1
    l1=[]
    for i in range(k):
        l1.append(s[i]+s[i+1])
        k-=1
    s=l1.copy()
    L.append(l1)
for i in L:
    print(i)
