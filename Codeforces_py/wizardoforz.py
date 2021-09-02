t=int(input())
for i in range(t):
    n=int(input())
    if(n==1):
        print(9)
    elif(n==2):
        print(98)
    elif(n==3):
        print(989)
    else:
        print(989,end="")
        q=0
        for i in range(0,n-3,1):
            q=q%10
            print(q,end="")
            q=q+1
        print()
          
