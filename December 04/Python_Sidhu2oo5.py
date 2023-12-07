s=input()
f=0
if s==s[::-1]:
    a=len(s)//2
    if len(s)%2==0:print(s[a-1:a+1])
    else:print(s[a-1:a+2])
else:
    for i in range(2,len(s)):
        if f:break
        for j in range(len(s)+1-i):
            b=s[j:i+j]
            if b==b[::-1]:
                print(b)
                f=1
                break;
    else:
        print('Error')
