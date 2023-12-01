n=int(input())
lis=list(eval(input().replace(' ',',')+','))
print(sum(lis))
print(lis.index(max(lis)))
