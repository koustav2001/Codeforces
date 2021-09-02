s=input()
cup,clw=0,0
for i in range(0,len(s)):
    if(s[i]>='A' and s[i]<='Z'):
        cup+=1
    else:
        clw+=1
if(cup>clw):
    print(s.upper())
else:
    print(s.lower())
