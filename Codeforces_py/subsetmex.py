t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=set()
    b=set()
    ans,ans1=0,0
    for i in l:
        if i in a:
            b.add(i)
        else:
            a.add(i)
    #print(list(a))
    #print(list(b))
    #c=list(a)
    k=0
    for i in range(101):
        if i not in a:
            k+=i
            break
    #print(ans)
    for i in range(101):
        if i not in b:
            k+=i
            break
    print(k)
    #print(ans1)
    #print(ans+ans1)
    t-=1
