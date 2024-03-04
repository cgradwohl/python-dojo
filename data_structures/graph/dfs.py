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

def dfs_recursive(G, vertex, target, visited):
  if vertex is None or vertex == target:
    return vertex
  visited.add(vertex)
  for child in G.adj[vertex]:
    if child in visited:
      continue
    result = dfs_recursive(G, child, target, visited)
    if result is not None:
      return result
  return None

def dfs_iterative(G, vertex, target):
  visited = set()
  s = [vertex]
  while len(s) > 0:
    node = s.pop()
    for child in G.adj[node]:
      if child in visited:
        continue
      if child == target:
        return child
      s.append(child)
      visited.add(child)


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

result1 = dfs_recursive(g, 7, 4, set())
print(result1)

result2 = dfs_iterative(g, 7, 4)
print(result2)


