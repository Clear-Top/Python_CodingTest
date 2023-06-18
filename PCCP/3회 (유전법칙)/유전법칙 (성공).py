def get_gene(query):
    # n_times: 세대를 거쳐올라갈때 나누는 횟수
    # m_times: 나눠지는 수
    n_times, m_times = query
    m_times = m_times - 1
    # 3세대면 2번나눔
    # 4세대면 3번나눔
    modula = []
    while n_times > 1:
        n_times -= 1
        modula.append(m_times % 4)
        m_times //= 4
    
    while modula:
        mo = modula.pop()
        if mo == 0:
            return "RR"
        elif mo == 3:
            return "rr"
    return "Rr"

def solution(queries):
    answer = []
    
    for query in queries:
        answer.append(get_gene(query))
    return answer

print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[2, 4]]))