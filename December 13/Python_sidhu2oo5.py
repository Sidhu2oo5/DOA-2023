a=[None,None,'ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b=input()
c=''
for i in b:
    if i.isalpha():
        for j in range(2,len(a)):
            if i in a[j]:
                c+=str(j)
    else:
        c+=str(i)
print(c)
