''' 다른풀이
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
'''

square = [
    [1,3],  # y>0, y<0
    [2,4]   # y>0, y<0
]
def solution(dot):
    dx = dot[0]
    dy = dot[1]
    slope = dy/dx
    row = 0 if slope > 0 else 1
    col = 0 if dy > 0 else 1 
    return square [row][col]