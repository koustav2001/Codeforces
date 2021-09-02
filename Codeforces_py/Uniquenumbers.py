t=int(input())
for i in range(t):
    ans=""
    n=int(input())
    if(n<10):
        print(n)
        continue
    elif(n>45):
        print(-1)
        continue
    else:
        for i in range(9,0,-1):
            if(n>=i):
                ans=str(i)+ans
                n=n-i
        print(ans)
                
