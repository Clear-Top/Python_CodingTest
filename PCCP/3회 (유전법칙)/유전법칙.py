from itertools import product
import sys

sys.setrecursionlimit(10**9)

def DFS(gen_seeds, queries, current_level):
    global total_seed
    str = ""
    seeds = [seed for seed in gen_seeds]
    new_gen_seeds = []
    # print(f"{current_level-1}세대 씨앗: {seeds}")
    if current_level == queries[0]+1:
        # 현재 생성된 세대가 맞다면
        total_seed.append("".join(gen_seeds))
    else:
        for seed in list(product(seeds, repeat=2)):
            str +=  "".join(seed)
            new_gen_seeds.append("".join(str))
            new_gen_seeds.sort()
            str = ""
        # print(f"{current_level}세대 씨앗: {new_gen_seeds}")
        for nth_seed in new_gen_seeds:
            DFS(nth_seed, queries, current_level+1)

def solution(queries):
    seeds = ['R', 'r']  # 1세대 자가수분의 시작
    gen_seeds = []
    str = ""
    current_level = 1
    global total_seed
    global answer

    for query in queries:
    #    answer = []
       total_seed = []
       DFS("".join(sorted(seeds)), query, current_level+1)
       answer.append("".join(sorted(total_seed[query[1]-1])))
       print(total_seed)
    return answer

total_seed = []
answer = []
# print(solution([[3, 5]]))	#["RR"]
# print(total_seed)
# print(solution([[3, 8], [2, 2]]))	#["rr", "Rr"]
print(solution([[3, 1], [2, 3], [3, 9]]))	#["RR", "Rr", "RR"]
# print(total_seed)
# print(solution([[4, 26]]))	#["Rr"]
# print(total_seed)