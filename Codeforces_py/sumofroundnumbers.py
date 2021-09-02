t=int(input())
for i in range(t):
    n=int(input())
    c=0
    cp=n
    while(n):
        if(n%10):
            c=c+1
        n=n//10
    print(c)
    i=1
    while(cp):
        if(cp%10):
            print(i*(cp%10),end=" ")
        cp=cp//10
        i=i*10
        
        
    
