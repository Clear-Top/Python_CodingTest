def solution(citations):
    citations.sort()
    start, end = 0, citations[-1]
    # print(start, end)
    max = 0
    while start <= end:
        cnt = 0
        h = (start+end)//2
        for cite in citations:
            if cite >= h:
                cnt += 1
        if cnt >= h:
            start = h + 1
        else:
            end = h - 1
    return end

print(solution([3, 0, 6, 1, 5]))