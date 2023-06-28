def solution(routes):
    # 최소 하나의 카메라는 필요
    camera_count = 1

    # 차량의 진출 시점을 기준으로 오름차순 정렬
    # 진입 시점을 기준으로 오름차순 정렬할 경우 교차 지점을 구할 수 없는 경우가 생김
    routes.sort(key=lambda x: x[1])

    camera_location = routes[0][1]

    # 다음 차량 진입, 진출 시점과 비교하면서 현재 예상 카메라 설치 위치보다 크다면 (더 멀어서 곂치지 않는 경우)
    # 현재 기준 위치에 카메라를 한 대 다는 걸로는 모자라기 때문에 카메라가 추가로 한 대 더 필요하고
    # 다음 차량 진출 시점을 예상 카메라 설치 위치로 갱신한다.
    for i in range(1, len(routes)):
        if camera_location < routes[i][0]:
            camera_count += 1
            camera_location = routes[i][1]

    return camera_count

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))