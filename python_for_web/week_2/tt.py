import networkx as nx

DG = nx.DiGraph()
DG.add_edge('S', 'a', weight=1)
DG.add_edge('a', 'b', weight=1)
DG.add_edge('a', 'c', weight=2)
DG.add_edge('b', 'd', weight=1)
DG.add_edge('b', 'e', weight=2)
DG.add_edge('c', 'e', weight=3)
DG.add_edge('c', 'f', weight=2)
DG.add_edge('d', 'T', weight=1)
DG.add_edge('e', 'T', weight=1)
DG.add_edge('f', 'T', weight=1)

print(nx.shortest_path(DG, 'S', 'T'))