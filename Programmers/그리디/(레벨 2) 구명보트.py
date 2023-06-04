def solution(people, limit):
    """
    아이디어: 제한을 넘지 않는 사람들을 최대한 꽉꽉 눌러담기
    아이디어: 작은것부터 넣기
    아이디어: Limit에서 먼넣은
    """
    # 사람들의 무게를 오름차순 정렬
    people.sort()
    boat_weight = 0
    light = 0
    heavy = len(people) - 1
    move = 0

    while people:
        if people[light] + people[heavy] <= limit and light < heavy:
            move += 1
            people.pop(light)
            people.pop(heavy-1)
            light = 0
            heavy = len(people) - 1
        elif people[light] + people[heavy] > limit and light < heavy:
            # boat_weight += people[light]
            heavy -= 1
            if light >= heavy:
                move += 1
                people.pop(light)
                light = 0
                heavy = len(people) - 1
                # boat_weight = 0
        else:
            # boat_weight += people[heavy]
            light += 1
            if light >= heavy:
                move += 1
                people.pop(heavy)
                light = 0
                heavy = len(people) - 1
                # boat_weight = 0
    return move

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))