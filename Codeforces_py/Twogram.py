n=int(input())
s=input()
ans,res=0,0
for i in range(0,len(s)-1):
    ans=0
    for j in range(0,len(s)-1):
        if(s[i]==s[j] and s[i+1]==s[j+1]):
            ans+=1
            if(res<ans):
                res=ans
                s1=s[i]+s[i+1]
print(s1)
