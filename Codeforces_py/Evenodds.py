
'''
#TLE
n,k=map(int,input().split())
lst=[]
lst1=[]
lst2=[]
for i in range(1,n+1):
    if i%2!=0:
        lst.append(i)
    else:
        lst1.append(i)
lst2=lst+lst1
#print(lst2)
print(lst2[k-1])
'''
n,k=map(int,input().split())
if(k<=(n+1)//2):#odd portion
    print((2*k)-1)
else:
    p=k-(n+1)//2
    print(2*p)

