def solution(box, n):
    return (box[0] // n) * (box[2] // n) * (box[2] // n)


print(solution([10, 8, 6], 3))
