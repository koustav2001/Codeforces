import math
n,m=map(int,input().split())
x=[int(x) for x in input().split()]
x.sort()
s=0
for i in x:
    if i<0 and m:
        s=s+abs(i)
        m-=1
    else:
        break
print(s)
