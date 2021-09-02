t=int(input())
for i in range(t):
    ans=0
    s=int(input())
    while(s!=0):
        if(s>=10):
            count=s//10
            ans+=count*10
            s=s%10
            s+=count
            #print(s)
        else:
            ans+=s
            s=0
    print(ans)
