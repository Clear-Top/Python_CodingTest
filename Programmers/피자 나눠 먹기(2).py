def solution(n):
    # 유클리드 호제법

    lcm = (6 * n) / GCD(n, 6)

    return int(lcm / 6)


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


print(solution(6))
