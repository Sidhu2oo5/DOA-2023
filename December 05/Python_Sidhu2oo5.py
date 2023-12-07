money=list(eval(input()))
avg=sum(money)/len(money)
cont=0
for i in money:
    if i>=avg:cont+=i
print(cont)
