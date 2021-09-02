n=int(input())
s=input()
c,c1=0,0
for i in range(0,len(s)):
    if(s[i]=='A'):
        c+=1
    else:
        c1+=1
if(c>c1):
    print("Anton")
elif(c==c1):
    print("Friendship")
else:
    print("Danik")
