'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
'''


def solution(answers):
    stu1_answer=[i % 5 + 1 for i in range(10000)]
    
    stu2_answer = []
    for i in range(10000):
        if i%5+1 != 2:
            stu2_answer.append(2)
            stu2_answer.append(i % 5 + 1)
    
    stu3_answer_rul = [3,1,2,4,5]
    stu3_answer = []
    for _ in range(10000):
        for c in stu3_answer_rul:
            stu3_answer.append(c)
            stu3_answer.append(c)


    num_correct = [0, 0, 0]
    for index,answer in enumerate(answers):
        if stu1_answer[index] == answer:
            num_correct[0] += 1
        if stu2_answer[index] == answer:
            num_correct[1] += 1
        if stu3_answer[index] == answer:
            num_correct[2] += 1

    answer = []
    for idx, val in enumerate(num_correct):
        if val == max(num_correct):
            answer.append(idx+1)
    
    return sorted(answer)

print(solution([1 for _ in range(10000)]))
print(solution([1,3,2,4,2]))