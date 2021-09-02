t=int(input())
for i in range(t):
    n=int(input())
    y=n%2020
    x=((n-y)//2020)-y
    if(x>=0 and x*2020+y*2021==n):
        print("YES")
    else:
        print("NO")
        
