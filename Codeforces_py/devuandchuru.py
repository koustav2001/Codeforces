n,k=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l)
if(s+(n-1)*10>k):
    print(-1)
else:
    print((k-s)//5)
