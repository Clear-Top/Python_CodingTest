import heapq
def solution(jobs):
    jobs.sort()
    
    tmp_jobs = []
    # jobs      : 소요시간 오름차순으로 정렬 (소요시간이 작은거부터 나옴)
    # tmp_jobs  : 현재시간보다 빨리 요청시간이 발생한 작업들을 소요시간 오름차순으로 정렬
    current_time = 0
    start_time = -1
    i = 0
    result = 0


    while i<len(jobs):
        for j in range(i, len(jobs)):
            # 소요시간이 짧더라도 바로 실행할 수 있는 것들부터 처리하려고
            if start_time < jobs[j][0] <= current_time:
                # 꺼내서 실행할때는 소요시간이 짧은 순서대로
                heapq.heappush(tmp_jobs, (jobs[j][1], jobs[j][0]))
        if tmp_jobs:
            # job[0]: 소요시간, job[1]: 요청시간
            job = heapq.heappop(tmp_jobs)       
            # print(f"{job}을 실행합니다")
            # print(f"현재시간: {start_time} 종료시간: {current_time+job[1]}")

            # job의 처리가 끝났다고 가정했을 때
            start_time = current_time
            current_time += job[0]
            result += current_time - job[1]
            i += 1
        else:
            current_time += 1

    return int(result/len(jobs))

print(solution([[0, 3], [1, 9], [2, 6]]))       # 9
print(solution([[0, 3], [10, 1]]))              # 2
print(solution([[7, 8], [3, 5], [9, 6]]))       # 9
print(solution([[1, 4], [7, 9], [1000, 3]]))    # 5
print(solution([[0, 1], [2, 2], [2, 3]]))       # 2