import sys
input = lambda: sys.stdin.readline().strip()
N = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0
count = 0

for i in data: #순회
    count+=1 #계속 카운팅을 함
    if count>=i: #카운팅 도중 해당 원소값에 도달하면 
        result+=i #해당 원소값 범위만큼 그룹카운팅
        count=0 #다시 카운팅 초기화
print(result)