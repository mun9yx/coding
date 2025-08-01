from collections import deque
def bfs(graph,i,visited):
    q = deque([i]) #시작 노드 큐에 삽입
    visited[i] = True #시작 노드 방문 표시

    while q: #큐가 빌 때까지 반복
        v = q.popleft() #현재 방문 노드 제거
        print(v,end= ' ') #방문 표시
        for i in graph[v]: #인접 노드 탐색
            if visited[i]==False: #인접 노드가 미방문 노드라면
                q.append(i) #큐에 삽입
                visited[i]=True #방문 표시

#11번 코드에서 DFS와 차이 파악 가능.
#BFS는 인접 노드를 모두 큐에 넣고, 선입된 순서대로 다시 인접노드를 순회함.
#DFS는 인접 노드 탐색 중, 바로 재귀함수를 통해 인접 노드를 순회함
#(인접의 인접의 인접의,,,,,,?)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9
bfs(graph,1,visited)