import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
s = list(map(int,input().split()))
po = [1,1]
for i in s:
    if 1<=po[0]<=5 and 1<=po[1]<=5:
        if i=='U': po[0]-=1 
        if i=='D': po[0]+=1
        if i=='L': po[1]-=1
        if i=='R': po[1]+=1
    else:
        pass
print(s[0],s[1])