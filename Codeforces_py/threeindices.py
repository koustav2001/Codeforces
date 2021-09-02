t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for i in range(1,len(l)-1):
        if(l[i]>l[i-1] and l[i]>l[i+1]):
            print("YES")
            print(i,i+1,i+2)
            f=1
            break
    if(f==0):
        print("NO")
    
    t-=1
