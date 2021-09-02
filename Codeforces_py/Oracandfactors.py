t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    p=0
    if(n%2==0):
        print(n+2*k)
        continue
    else:
        for i in range(n,1,-1):
            if(n%i==0):
                p=i
        print(n+p+2*(k-1))
    
    
