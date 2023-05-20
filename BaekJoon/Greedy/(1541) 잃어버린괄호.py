'''아이디어
+ - 기준으로 여러개로 쪼개기
strip 함수로 맨앞에 0 들을 지우기
첫 - 바로 앞부터 마지막까지 중괄호 씌워서 식계산하기 
'''
eqa = input()
temp = []

# temp = list(map(int, eqa.split("-")))
temp = eqa.split("-")

result = 0
for sub_eqa in temp[1:]:
    result += sum(map(int, sub_eqa.split("+")))


print(result)

