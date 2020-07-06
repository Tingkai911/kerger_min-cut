import random, copy

def main():
    
    G, edges, vertices = [], [], []
    with open('kargerMinCut.txt', 'r') as file:
            for line in file.readlines():
                    G.append(line)

    # create the list of vertices and edges
    for i in range(len(G)):
        s = G[i].split()
        vertices.append(int(s[0]))
        for j in range(1, len(s)):
            # remove duplicates
            if [int(s[0]), int(s[j])] not in edges:
                edges.append([int(s[0]), int(s[j])])
    
    # print(G)
    # print(vertices)
    # print(edges)
    # print(len(edges))

    print(karger(100, vertices, edges))


# run the karger function n times
def karger(n, vertices, edges):
    i = 0
    count = float('inf') 
    while i < n:
        data_v = copy.deepcopy(vertices)
        data_e = copy.deepcopy(edges)
        min_cut = contact(data_v, data_e)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count


# using karger random contraction
def contact(vertices, edges):
    
    while len(vertices) > 2:

        # randomly selecting a remaning edge
        index = random.randint(0, len(edges) - 1)
        # remove the edge between u and v
        [u, v] = edges.pop(index)
        # remove v from the vertices -> u and v combine into a super vertex
        vertices.remove(v)
        newEdges = []
        for i in range(len(edges)):
            # makes the path that starts from v to start from u instead
            if edges[i][0] == v:
                edges[i][0] = u
            # makes the path that ends at v to end at u instead
            elif edges[i][1] == v:
                edges[i][1] = u
            # remove self-loops
            if edges[i][0] != edges [i][1]:
                newEdges.append(edges[i])
        edges = newEdges
                
    return calculate(edges)


def calculate(edges):
    count = 0
    check =  edges[0]
    for edge in edges:
        if edge == check:
            count = count + 1
    return count


if __name__ == "__main__":
    main()