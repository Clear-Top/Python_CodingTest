def find_root(ptable, island):
    if ptable[island] == island:
        return island
    return find_root(ptable, ptable[island])


def union(ptable, island1, island2):
    parent1 = find_root(ptable, island1)
    parent2 = find_root(ptable, island2)

    if parent1 < parent2:
        ptable[parent2] = parent1
    else:
        ptable[parent1] = parent2


def solution(n, costs):
    edges = []

    for row in costs:
        island1, island2, cost = row
        edges.append((cost, island1, island2))
        
    edges.sort()

    ptable = [0] * n
    for i in range(n):
        ptable[i] = i

    min_cost = 0
    for edge in edges:
        cost, island1, island2 = edge
        if find_root(ptable, island1) != find_root(ptable, island2):
            union(ptable, island1, island2)
            min_cost += cost

    return min_cost

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))