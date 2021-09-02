t=int(input())
while(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    i=1
    r=0
    while(i<=1000):
        if i in l:
            i+=1
            r+=1
            continue
        else:
            if x>0:
                x-=1
                r+=1
                #print(i,x)
                i+=1
            else:
                break
    print(r)      
    t-=1
