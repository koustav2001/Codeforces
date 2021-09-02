n=int(input())
s=str(n)
last=int(s[:-1])
#print(int(last))
second_last=int(s[:-2]+s[-1])
#print(int(second_last))
if(n>last and n>second_last):
    print(n)
if(n<last and n<second_last):
    if(last>second_last):
        print(last)
    else:
        print(second_last)
