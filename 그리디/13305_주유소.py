import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
total,d,f = 0,0,0
for i in range(len(price)-1):
    if f==1: #정류소와 거리가 일치하지 않을시
        if i==d: # 일치하게 된다면
            f=0 #초기화
        else: #일치하지 않는다면 
            continue #일치할때 까지 반복문 조건문으로 이동
    if price[i]>price[i+1]: #다음 정류소 가격이 저렴하면
        total+=price[i]*distance[d] #현재 정류소 가격 적용을 중단
        d+=1
    else: #다음 정류소 가격이 더 비싸면
        for j in range(i+1,len(price)): #현재 정류소 기준으로 다음 거리들에 대한 가격 측정
            if price[j]>price[i]: #현재 정류소가 계속 저렴하다면
                total+=price[i]*distance[d] #현재 정류소 기준으로 가격 측정
                d+=1 #거리 이동
            else: #다음 정류소가 더 저렴하다면
                total+=price[i]*distance[d] #현재 정류소까지 거리 측정 후
                d+=1 #거리 이동 후
                break #현재 정류소에 대한 측정 중지 
        if i!=d: #현재 정류소와 인접 거리가 불일치 할시
            f=1 #플래그 변수
print(total)
