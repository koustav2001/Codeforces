n=int(input())
meat=[]
money=[]
for i in range(n):
    x=[int(x) for x in input().split()]
    a=x[0]
    b=x[1]
    meat.append(a)
    money.append(b)
ans=0
m=money[0]
for i in range(len(meat)):
    if money[i]<m:
        m=money[i]
    ans=ans+m*meat[i]
print(ans)
#print(meat)
#print(money)
