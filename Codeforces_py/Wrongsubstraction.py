n,k=map(int,input().split())
count=0
while n:
    if(n%10!=0):
        n=n-1
        count+=1
        #print(n,count)
    else:
        n=n//10
        count+=1
        #print(n)
    if(count==k):
        break
print(n)
