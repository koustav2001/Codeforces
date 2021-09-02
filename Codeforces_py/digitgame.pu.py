t=int(input())
while(t):
    n=int(input())
    s=input()
    a,b=[],[]
    for i in range(0,len(s)):
        if(i%2==0):
            a.append(int(s[i])%2)
        else:
            b.append(int(s[i])%2)

    if(len(s)%2==0):
        if(b.count(0)>0):
            print(2)
        else:
            print(1)
    else:
        if(a.count(1)>0):
            print(1)
        else:
            print(2)
                
            
    t-=1
