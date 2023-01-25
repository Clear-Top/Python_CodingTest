'''
문제: 알파벳대문자들과 숫자(0-9)들이 일렬로 주어질때,
    알바벳들이 오름차순으로 정렬되어 출력되고
    숫자들은 모두 더하여 문자들 이후에 출력되어야 한다.
'''

# 시간: 1초
# 메모리: 128MB
# 입력: 하나의 문자열이 주어진다 (문자열=[1,10,000])

import time

def realignString():
    tmp = list()
    tmp_sum = 0
    
    for c in S:
        if 'A'<=c<='Z':
            tmp.append(c)
        elif '0'<=c<='9':
            tmp_sum += int(c)
    tmp.sort()
    return tmp, str(tmp_sum)

S = input()

start = time.time()

result_string, result_sum = realignString()
result_string+=result_sum

print(''.join(result_string))

end = time.time()

print(f"{end-start:.3f} seconds")