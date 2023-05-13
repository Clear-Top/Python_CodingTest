
''' 다른풀이
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])
'''
def solution(n, control):
    dict ={
        'w':'+1',
        's':'-1',
        'd':'+10',
        'a':'-10'
    }
    
    list = [dict[control[i]] for i in range (len(control))]
    print(list)
    
    temp = eval(''.join(list))

n, control = 0, "wsdawsdassw"

solution(n, control)