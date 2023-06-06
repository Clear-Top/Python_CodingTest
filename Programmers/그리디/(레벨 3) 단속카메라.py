def solution(routes):
    current_camera_pos = (routes[0][0], routes[0][1])
    num_camera = 1

    for i in range(1,len(routes)):
        come_in, come_out = routes[i]
        if come_in in range(current_camera_pos[0], current_camera_pos[1]+1):
            current_camera_pos = (max(come_in,current_camera_pos[0]), min(come_out, current_camera_pos[1]))
            print(f"{i+1}번째 자동차는 겹칩니다.")
        else:
            num_camera += 1
            print(f"{i+1}번째 자동차는 겹치지 않습니다. 카메라를 새로 추가합니다")
            current_camera_pos = (come_in, come_out)
    return num_camera

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-3, -2], [-2, -1], [-1, 0], [0, 1]]))  #3
print(solution([[0, 10], [4, 6], [7, 9]]))  #2
print(solution([[0, 10], [4, 6], [5, 7]]))  #1