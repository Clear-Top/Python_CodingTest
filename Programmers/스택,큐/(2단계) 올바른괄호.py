def solution(blanket):
    """
    입력: 괄호 문자열
    출력: Boolean

    아이디어:
    1. '(' 는 무조건 push
    2. ')' 는 스택의 가장위에 '(' 를 pop
    3. pop 할때 스택이 비어있으면 무조건 짝이 안맞는 경우이다.
    4. 마지막으로 스택에 내용물이 있으면 False (왜냐면 (가 잔재할 수 있다는 것이므로, 이것은 짝이 제대로 안맞는다는 의미)
    """

    # 괄호의 스택화
    stack = []
    for c in blanket:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

if __name__=="__main__":
    print(solution("(()("))