p = "qwertyuiopasdfghjkl;zxcvbnm,./"
shift=input()
s=input()
res=""
a=-1 if shift=='R' else 1
for i in s:
    res+=p[p.find(i)+a]
print(res)
