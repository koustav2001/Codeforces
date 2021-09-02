t=int(input())
c2,c3=0,0
for i in range(t):
    n=int(input())
    while((n%2)!=0):
        c2+=1
        n=n//2
    while((n%3)!=0):
        c3+=1
        n=n//3
    print(c2,c3)
    '''if(n!=1 or c2>c3):
        print("-1")
    else:
        print(c3-c2+c3)
'''

        
        
