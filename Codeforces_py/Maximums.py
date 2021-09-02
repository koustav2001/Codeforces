a=[]
n=int(input())
x=[int(x) for x in input().split()]
m=0
#print(x)
for i in range(0,len(x)):
    a.append(x[i]+m)
    print(a[i],end=" ")
    m=max(a[i],m)

