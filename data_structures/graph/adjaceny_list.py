class GraphADT:
  def __init__(self) -> None:
    self.adj= {}

  def add_vertex(self, u: int) -> None:
    if u not in self.adj:
      self.adj[u] = []
  def add_edge(self, u: int, v: int) -> None:
      if u not in self.adj or v not in self.adj:
        raise Exception("noop.")
      if u not in self.adj[v]:
        self.adj[v].append(u)
      if v not in self.adj[u]:
        self.adj[u].append(v)


g = GraphADT()
g.add_vertex(7)
g.add_vertex(9)
g.add_vertex(17)
g.add_vertex(21)
g.add_vertex(21)

g.add_edge(7, 9)
g.add_edge(7, 17)
g.add_edge(7, 21)
g.add_edge(7, 21)
g.add_edge(17, 21)
g.add_edge(17, 21)

# print(g.adj)

s = set()
s.add(7)
s.add(9)
s.add(17)
s.add(7)


d = {}
d[7] = [9, 17]
d[8] = [9, 17]
d[7].remove(9)
print(list(d.keys()))
