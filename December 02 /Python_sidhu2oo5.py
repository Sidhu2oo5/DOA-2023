lis=eval(input())
lis2=list(set(lis))
print(lis2)
lis3=[lis.count(i) for i in lis2]
print(lis3)
