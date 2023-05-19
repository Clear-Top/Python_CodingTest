'''아이디어
+ - 기준으로 여러개로 쪼개기
strip 함수로 맨앞에 0 들을 지우기
첫 - 바로 앞부터 마지막까지 중괄호 씌워서 식계산하기 
'''
formula_str = input()
formula_modify = []
for i in formula_str:
    if i=='+' or i=='-':
        list_str = list(formula_str[:formula_str.find(i)])
        formula_modify.append(list_str)
    else:
        formula_modify.append([i])
        
print(formula_modify)
        # formula_modify.append(list)
# print(formula_modify)
# print(formula_str[:formula_str.find('-')])
