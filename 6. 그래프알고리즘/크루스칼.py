# 무방향그래프 사이클판별 - Find
def find_root(ptable, v):
    if ptable[v] == v:
        return v
    return find_root(ptable, ptable[v])

# 무방향그래프 사이클판별 - Union
def union(ptable, v1, v2):
    v1 = find_root(ptable, v1)
    v2 = find_root(ptable, v2)
    if v1<v2:
        ptable[v2] = v1
    else:
        ptable[v1] = v2
        
# 노드(v)와 간선(e)개수 입력받기
v, e = map(int, input().split())
edges = []

# 간선정보(정점1-정점2-비용) 입력받기
for _ in range(e):
	v1, v2, cost = map(int, input().split())
	edges.append((cost, v1, v2))	# cost 오름차순으로 정렬해야하므로

edges.sort()

# 부모테이블 초기화
ptable = [0] * v

# 자신의 부모가 자기자신이 되도록 설정
for i in range(v):
	ptable[i] = i

# 최소비용
min_cost = 0

for edge in edges:
    cost, v1, v2 = edge	# 언패킹  
    if find_root(ptable, v1) == find_root(ptable, v2):
        continue 
    union(ptable, v1, v2)
    min_cost += cost

print(min_cost)