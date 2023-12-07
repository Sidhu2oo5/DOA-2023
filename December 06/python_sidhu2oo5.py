words=list(eval(input()))
dcode=[words[0]]
c=0
for i in range(1,len(words)):
    if len(words[i])!=len(words[i-1]):
        break
    else:
        for j in range(len(words[i])):
            if words[i][j]==words[i-1][j]:
                c+=1
        if c>=len(words[i])-1:
            dcode.append(words[i])
print(dcode)
