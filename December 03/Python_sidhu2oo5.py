N=int(input())
H=eval(input())
a=-1
while(H!=sorted(H)):
    for i in range(N+a):
        if H[a]<H[i]:
            H.pop(a)
            break;
    else:
        a-=1
print(len(set(H)))
