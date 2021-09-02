t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a==b):
        print(0)
    else:
        c=abs(a-b)
        if(c):
            print((c/10)+1)
        else:
            print((c/10))
