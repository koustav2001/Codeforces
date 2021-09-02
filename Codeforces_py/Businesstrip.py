k=int(input())
x=[int(x) for x in input().split()]
#print(x)
x.sort(reverse=True)
#print(x)
c,s=0,0
flag=0
if k==0:
    flag=1
    print(0)
else:
    for i in x:
        s=s+i
        c+=1
        if(s>=k):
            flag=1
            print(c)
            break
        else:
            flag=0

if(flag==0):
    print(-1)
    

