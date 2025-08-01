def dfs(graph,i,visited):
    visited[i]=True #재귀할 때마다 노드 방문시 True
    v = i #현재 노드 표시
    print(v,end= ' ') #방문한 현재 노드 출력
    for i in graph[v]: #현재 노드기준으로 인접 노드 순회
        if visited[i]==False: #인접 노드가 미방문 노드라면
            dfs(graph,i,visited) #해당 노드 탐색

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
dfs(graph,1,visited)
