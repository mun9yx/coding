import sys
input = lambda: sys.stdin.readline().strip()
s = input().split('-')
l = []

for i in s:
    tmp = list(map(int,i.split('+')))
    l.append(sum(tmp))

total = l[0]
for i in range(1,len(l)):
    total-=l[i]
print(total)