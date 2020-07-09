# kerger_min-cut
Find the minimum cut of an undirected graph using Kerger's algorithm

While there are more than 2 vertices:
- pick a remaining edge (u,v) uniformly at random
- merge (or “contract” ) u and v into a single vertex
- remove self-loops

return cut represented by final 2 vertices.
two different implementations avaliable
