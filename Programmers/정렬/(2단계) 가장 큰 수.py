def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(reverse=True, key=lambda x: x*3)
    return str(int("".join(numbers_str)))
    
if __name__ == "__main__":
    print(solution([3, 30, 34, 5, 9]))