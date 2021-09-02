n=int(input())
c=0
while(n):
    d=n%10
    n=n//10
    #print(n)
    if(d==4 or d==7):
        c+=1
#print(c)
if(c==4 or c==7):
    print("YES")
else:
    print("NO")
