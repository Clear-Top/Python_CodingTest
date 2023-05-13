'''
(내장)      sorted: sorted(list) => list 와 별개로 새로운 리스트를 생성 후 리스트를 반환
(리스트)    sort: list.sort() => list 자체를 정렬시킴
'''

'''
(내장)      reversed: reversed(list) => list 와 별개로 새로운 리스트를 뒤집고 반복자객체를 반환
(리스트)    reverse: list.reverse() => list 자체를 뒤집음
'''

print([1,2,3].reverse())    # None
print(reversed([1,2,3]))    # 반복자객체 (for 문에 바로 사용가능)
print([1,2,3].sort())       # None
print(sorted([1,2,3]))      # 뒤집힌 새로운 리스트를 반환