t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    f=1
    s=0
    for i in range(0,len(l)):
       s+=l[i]
       if(s<i*(i+1)//2):
           f=0
    if(f):
        print("YES")
    else:
        print("NO")
    t-=1                                       #1,1,1,1
    
