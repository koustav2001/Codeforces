t=int(input())
for i in range(t):
    n=int(input())
    c=10**9
    for i in range(2,c+1):
        p=(2**i)-1
        if(n%p==0):
            print(n//p)
            break
            
            
            
    
