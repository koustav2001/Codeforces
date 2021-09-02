a,b=map(int,input().split())
c=min(a,b)
d=max(a,b)
if(d-c==1 or d-c==0):
    e=0
else:
    e=(d-c)//2
print(c,e)
    
