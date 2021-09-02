n=int(input())
s=input()
czero,cone=0,0
for i in range(0,len(s)):
    if(s[i]=='1'):
        cone+=1
    else:
        czero+=1
if(czero==cone):
    print(0)
else:
    print(abs(czero-cone))
        
