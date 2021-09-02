n=int(input())
x=list(map(int,input().split(' ')))
for i in range(n):
    if(i==0):
        print(abs(x[1]-x[0]),abs(x[-1]-x[0]))
    elif(i==n-1):
        print(abs(x[-1]-x[-2]),abs(x[-1]-x[0]))
    else:
        mi=min(abs(x[i]-x[i-1]),abs(x[i+1]-x[i]))
        ma=max(abs(x[-1]-x[i]),abs(x[0]-x[i]))
        print(mi,ma)
        
    
