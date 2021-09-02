n=int(input())
x=[int(x) for x in input().split()]
odd,even=0,0
for i in range(n):
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(min(odd,even))

