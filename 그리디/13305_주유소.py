import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
total = 0
d = 0
f= 0
for i in range(len(price)-1):
    if f==1:
        if i==d:
            f=0
        else:
            continue
    if price[i]>price[i+1]:
        total+=price[i]*distance[d]
        d+=1
    else:
        for j in range(i+1,len(price)):
            if price[j]>price[i]:
                total+=price[i]*distance[d]
                d+=1
            else:
                total+=price[i]*distance[d]
                d+=1
                break
        if i!=d:
            f=1 
print(total)