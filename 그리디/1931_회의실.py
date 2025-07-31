import sys
input = lambda: sys.stdin.readline().strip()
N = int(input())
arr = []
cnt = 1
for i in range(N):
    a,b = map(int,input().split())
    arr.append([a,b])
arr = sorted(arr,key=lambda x:(x[1],x[0]))
end = arr[0][1]
for i in range(1,len(arr)):
    if arr[i][0]<end: #다음 시작시간이 이전 종료시간보다 빠르면
        pass #패스
    else: #같거나 이후시간이면 카운팅
        end = arr[i][1]
        cnt+=1

print(cnt)