import random, copy

# create a dictionary with vertices and keys and edges as values
data = open("kargerMinCut.txt","r")
G = {}
for line in data:
    lst = [int(s) for s in line.split()]
    G[lst[0]] = lst[1:]   
# print(G)

# choose a random edges 
def choose_random_key(G):
	# the vertices are the keys of G
    v1 = random.choice(list(G.keys()))
	# the end point of the edge are one of the values in G[key]
    v2 = random.choice(list(G[v1]))
    return v1, v2


def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
		# merge/contract v1 and v2 into a single vertex
        G[v1].extend(G[v2])
		# replaces all v2 with v1
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
		# remove self-loops 
        while v1 in G[v1]:
            G[v1].remove(v1)
		# delete v2, now that v1 and v2 is a single vertex
        del G[v2]
	# there is only 2 keys in G at this stage
    for key in G.keys():
		# count the number of edges
        length.append(len(G[key]))
    return length[0]


# run the karger function n times
def operation(n):
    i = 0
    count = 10000   
    while i < n:
        data = copy.deepcopy(G)
        min_cut = karger(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count


print(operation(100))