s=input()
for i in range(0,len(s)-2):
    if(s[i]=='W' and s[i+1]=='U' and s[i+2]=='B'):
        i=i+3
        print(end=" ")
    else:
        print(s[i])
