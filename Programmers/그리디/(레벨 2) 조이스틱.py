def move_cursor(cursor, name, direction):
    cnt = 0
    if direction == -1:
        while True:
            cursor = (cursor + direction + len(name)) % len(name)
            if name[cursor] != 'A':
                cnt += 1
                break
            else:
                cnt+=1
    else:
        while True:
            cursor = (cursor + direction) % len(name)
            if name[cursor] != 'A':
                cnt += 1
                break
            else:
                cnt += 1
    return (cnt, cursor)

def solution(name):
    """ 아이디어
    1. 입력받은 name의 길이만큼 A-- 문자열을 생성
    2-1. 문자변경: 다음 or 이전 알파벳 방향을 결정해서 카운팅
    2-2. 커서이동: 오른쪽이 A 라면 왼쪽으로 커서이동, 왼쪽이 A라면 오른쪽으로 커서이동
    3. 첫 커서로 다시 돌아올때까지 반복

    ** 사용할 내장함수: chr(65) ord('A') 
    ** A(65) B C D E F G J I J K L(76) M N O P Q R S T U V W X Y Z(90)
    ** A 를 오른쪽 조작해서 L을 만드려면: 'L'-'A' = 11번 오른쪽조작
    ** A 를 왼쪽 조작해서 L을 만드려면: 'Z'-'L' + 1 = 15
    """

    # new_name = chr(65) * len(name)
    new_name = [0] * len(name)
    # print(new_name)

    print("**********")
    print(f"만들어야 할 이름: {name}")
    print(f"현재 이름: {new_name}")
    print("**********")

    move_stick = 0 # 조이스틱 움직인 횟수
    cnt_changed = 0 # 왼쪽/오른쪽 커서이동할때마다 1씩 증가
    cursor = 0   # name 에서 타겟문자 위치

    while cnt_changed < len(name):
        if ord(name[cursor]) - ord('A') < ord('Z') - ord(name[cursor]) + 1:
            move_stick += ord(name[cursor]) - ord('A')
            new_name[cursor] = chr(ord('A') + ord(name[cursor]) - ord('A'))
            print(f"조이스틱을 위로 {ord(name[cursor]) - ord('A')}번 움직여 변경")
            print(f"현재까지 변경된 이름: {new_name}")
            # 다음알파벳으로 이동
        else:
            move_stick += ord('Z') - ord(name[cursor])
            new_name[cursor] = chr(ord('Z') - (ord('Z') - ord(name[cursor])))
            print(f"조이스틱을 아래로 {ord('Z') - ord(name[cursor])}번 움직여 변경")
            print(f"현재까지 변경된 이름: {new_name}")
            # 이전알파벳으로 이동
        cnt_changed+=1
        if name[(cursor+1)%len(name)] == 'A':
            # 커서 왼쪽으로 이동
            print("커서 왼쪽으로 ",end="")
            info = move_cursor(cursor, name, -1)
        else:
            # 커서 오른쪽으로 이동
            print("커서 오른쪽으로 ",end="")
            info = move_cursor(cursor, name, +1)
        cursor = info[1]
        print(f"{info[0]} 번 이동하여 {cursor}번째로 커서이동")
        print(f"현재까지 고려한 횟수: {cnt_changed}")
        print()
        move_stick += info[0]
        cnt_changed += info[0]
    return move_stick

print(solution("JAZ"))
print()
print(solution("JEROEN"))
print()
print(solution("JAN"))