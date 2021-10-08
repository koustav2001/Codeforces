t=int(input())
for i in range(t):
    s=input()
    czero,cone=0,0
    for i in range(0,len(s)):
        if(s[i]=='0'):
            czero+=1
        else:
            cone+=1
    m=min(cone,czero)
    if(m%2==0):
        print("net")
    else:
        print("DA")
