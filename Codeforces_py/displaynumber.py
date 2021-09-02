t=int(input())
while(t):
    s=""
    n=int(input())
    if(n%2==0):
        for i in range(1,n//2+1):
            s=s+"1"
    else:
        s=s+"7"
        n=n-3
        for i in range(1,n//2+1):
            s=s+"1"
    print(int(s))
    t-=1
