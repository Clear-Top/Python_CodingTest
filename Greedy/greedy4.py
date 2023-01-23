'''
문제: N명의 사람들은 각각 특정 숫자카드를 가지고 있다.
    X의 숫자카드를 가진 사람은 반드시 X명 이상으로 구성된 그룹에 속해야만 한다.
    N명의 사람들로 나누어질수있는 최대 그룹 수는 몇개인가?
'''
import time

def greedy4():
    global people
    group = 0   # 그룹 수
    count = 0   # 현재 그룹의 사람 수
    list_people.sort()
    
    for i in list_people:
        count+=1
        if count >= i:
            group+=1
            count = 0
    return group


people = int(input())
list_people = list(map(int, input().split()))

start = time.time()

group = greedy4()
print(group)

end = time.time()

print(f"{end-start:.3f} seconds")