def solution(people, limit):
    # 사람들의 무게를 오름차순 정렬
    people.sort()
    start = 0
    end = len(people) - 1
    move = 0

    while start <= end:
        if people[start] + people[end] <= limit:
            move += 1
            start += 1
            end -= 1
        else:   # people[start] + people[end] > limit:
            move += 1
            end -= 1
    return move
    
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))