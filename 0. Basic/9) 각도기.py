'''다른 풀이
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
'''

def solution(angle):
    evaluation = dict(zip(["0<{angle}<90","{angle}==90","90<{angle}<180","{angle}==180"],[1,2,3,4]))
    
    for i in evaluation:
        str = i.replace("{angle}",repr(angle))
        if eval(str) == True:
            print(evaluation[i])
    
    # for i in range (len(evaluation)):
    #     str = "f\'" + evaluation[i]
    #     print(str)
        
# solution(70)    # 1
# solution(90)    # 3
solution(180)   # 4