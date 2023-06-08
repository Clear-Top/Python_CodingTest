import heapq
def solution(jobs):
    '''
    job[0]: 요청시간
    job[1]: 소요시간 
    '''
    heapq.heapify(jobs)

    tmp_jobs = []
    for job in jobs:
        # 소요시간 기준으로 오름차순 정렬
        heapq.heappush(tmp_jobs, (job[1], job[0]))

    avg_time = 0
    current_time = 0
    start_time = 0
    num = 0
    while tmp_jobs:
        '''
        job[0]: 소요시간
        job[1]: 요청시간 
        '''
        job = heapq.heappop(tmp_jobs)
        print(f"{start_time}ms 시점에 {job[0]} 걸리는 작업 요청이 들어옵니다.")
        current_time += (start_time + job[0] - job[1])
        # print(f"현재작업은 {job[1]}ms 부터 대기하다가, {start_time}ms 시점에 작업을 시작해서 {start_time + job[0]}ms 시점에 작업완료 (요청에서 종료까지: {start_time + job[0] - job[1]}ms)")
        start_time += job[0]
        num += 1

    return int(current_time / num)

print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[0, 3], [1, 9], [2, 6]]))