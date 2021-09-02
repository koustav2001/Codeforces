t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if(k>n):
        print(k-n)
    else:
        if((n-k)%2==0):
            print(0)
        else:
            print(1)
