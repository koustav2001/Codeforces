s=input()
f=0
for i in range(0,len(s)):
    if(s[i]=='H' or s[i]=='Q' or s[i]=='9'):
        f=1
        break
    else:
        f=0
if(f==1):
    print("YES")
else:
    print("NO")
