'''
If the number x has an odd divisor, then it has an odd prime divisor.
As the only even prime divisor is 2 so if its not divisble by odd prime divisors
'''

t=int(input())
for i in range(t):
    n=int(input())
    if(n%2!=0):
        print("YES")
    else:
        p=n
        while(p%2==0):
            p=p//2
        if(p>1):
            print("YES")
        else:
            print("NO")
