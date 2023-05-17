def solution(age):
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    ages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = {key: value for key, value in zip(ages, alpha)}
    return "".join([d[int(i)] for i in str(age)])


print(solution(51))
