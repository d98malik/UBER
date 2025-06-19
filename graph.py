from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C'],
    'Z': ['V']
}


# BFS
def dfs(graph,node,visited_nodes = set()):
    if node not in visited_nodes:
        print(node)
        visited_nodes.add(node)
        for node in graph[node]:
            dfs(graph,node,visited_nodes)

# DFS


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

if __name__=="__main__":
    bfs(graph,"A")