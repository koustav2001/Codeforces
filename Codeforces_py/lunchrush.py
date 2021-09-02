n,k=map(int,input().split())
l=[]
while(n):
    f,t=map(int,input().split())
    if(t<=k):
        f1=f
        l.append(f1)
    else:
        f2=f-(t-k)
        l.append(f2)
    n-=1
        
print(max(l))
