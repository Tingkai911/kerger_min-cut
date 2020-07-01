# kerger_min-cut
Find the minimum cut of an undirected graph using Kerger's algorithm

While there are more than 2 vertices:
• pick a remaining edge (v1,v2) uniformly at random
• merge (or “contract” ) v1 and v2 into a single vertex
• remove self-loops
return cut represented by final 2 vertices.
