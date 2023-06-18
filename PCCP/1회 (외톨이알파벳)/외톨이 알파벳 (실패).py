def solution(input_string):
    '''
    1. 외톨이 알파벳 조건
    1) 두 번 이상등장
    2) 연속되어 있으면 안됨

    2. 출력:
    1) 외톨이 알파벳들을 공백없이 알파벳순서대로 출력
    
    4. 제약사항: 
    - 스트링길이 1~2600
    - 모든 알파벳은 소문자로만 구성

    '''

    
    # 혼자힘으로 해보기
    answer = []
    
    # 1. 알파벳 덩어리 찾기
    pos = 0
    end_pos = 0
    current_char = ""
    while pos < len(input_string):
        if current_char == input_string[pos]:
            current_char += input_string
            end_pos+=1
        else:
            current_char = ""
            current_char += input_string[pos]
            pos 
        current_char_index = pos
        flag = True # 가정: 무조건 외톨이 알파벳이다
        for index, c in enumerate(input_string[end_pos+1:]):
            if c == current_char:
                current_char_index == index+1
                flag = False
                break
                # 연속됨
        if flag:
            answer.append(current_char)

print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))