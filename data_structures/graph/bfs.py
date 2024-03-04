from collections import deque
def bfs(G, vertex, target):
  visited = set()
  queue = deque([vertex])

  while len(queue) > 0:
    node = queue.popleft()
    for child in G.adj[node]:
      if child in visited:
        continue
      if child == target:
        return child
      visited.add(child)
      queue.append(child)

class Graph:
  def __init__(self) -> None:
    self.adj = {}
  
  def add_vertex(self, v: int) -> None:
    if v not in self.adj:
      self.adj[v] = []

  def add_edge(self, u: int, v: int):
    if u not in self.adj or v not in self.adj:
      return
    if u not in self.adj[v]:
      self.adj[v].append(u)
    if v not in self.adj[u]:
      self.adj[u].append(v)
g = Graph()
g.add_vertex(4)
g.add_vertex(7)
g.add_vertex(9)
g.add_vertex(17)
g.add_vertex(21)
g.add_vertex(42)

g.add_edge(7, 9)
g.add_edge(7, 21)
g.add_edge(7, 17)

g.add_edge(17, 21)
g.add_edge(17, 7)
g.add_edge(17, 4)

g.add_edge(4, 17)
g.add_edge(4, 21)
g.add_edge(4, 9)

result = bfs(g, 7, 4)
print(result)
