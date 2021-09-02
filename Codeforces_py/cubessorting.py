t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for i in range(len(l)-1,-1,-1):
        if(l[i]>=l[i-1]):
            f=1
            break
    if(f):
        print("YES")
    else:
        print("NO")
    t-=1
