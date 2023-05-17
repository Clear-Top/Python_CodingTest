def solution(order):
    t = (3, 6, 9)
    print("order=" + str(order))
    print("tuple=" + str(t))

    answer = [i for i in str(order) if i in str(t)]
    return len(answer)


print(solution(33333))
