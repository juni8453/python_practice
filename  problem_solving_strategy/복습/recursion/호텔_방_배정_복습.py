# 시간 초과 발생 로직
def find_empty_room(want_room, answer):
    # 방이 비어서 바로 배정이 되는 경우 (종료 조건)
    # 선형 탐색 시간을 줄이기 위해 answer 를 딕셔너리로 사용
    if want_room not in answer:
        answer[want_room] = 1
        return

    # 방이 비어서 바로 배정이 안되는 경우 (계속해서 재귀 호출)
    return find_empty_room(want_room + 1, answer)

def solution(k, room_number):
    answer = dict()

    for want_room in room_number:
        find_empty_room(want_room, answer)

    return list(answer)

    return answer


print(solution(10, [1,3,4,1,3,1]))

# 시간 초과 개선 로직
def find_empty_room(want_room, answer):
    # 종료 조건 (빈 방이 있을 때)
    if want_room not in answer:
        answer[want_room] = want_room + 1
        return want_room # 원래 원했던 방 반환

    empty_room = find_empty_room(answer[want_room], answer)
    answer[want_room] = empty_room + 1
    return empty_room

def solution(k, room_number):
    answer = dict()

    for want_room in room_number:
        find_empty_room(want_room, answer)

    return list(answer)

    return answer


print(solution(10, [1,3,4,1,3,1]))


# 총 방은 k 개 있다.
# 1. 한 번에 한 명씩 신청 순서대로 방을 배정
# 2. 고객은 투숙을 원하는 방 번호를 제출
# 3. 고객이 원하는 방이 비었다면 즉시 배정
# 4. 고객이 원하는 방이 이미 배정되어 있다면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정

# ex)
# k = 10, room_number = [1,3,4,1,3,1] 이라면,

# 1 번방을 원함 -> 1 번방은 빈 상태 -> 1 번방 배정 - 현재 빈방 [2,3,4,5,6,7,8,9,10]
# 3 번방을 원함 -> 3 번방은 빈 상태 -> 3 번방 배정 - 현재 빈방 [2,4,5,6,7,8,9,10]
# 4 번방을 원함 -> 4 번방은 빈 상태 -> 4 번방 배정 - 현재 빈방 [2,5,6,7,8,9,10]

# 1 번방을 원함 -> 1 번방은 이미 찬 상태 -> 현재 빈방 확인 (1 번방 보다 큰 비어있는 방) -> 2 번방 배정 - 현재 빈방 [5,6,7,8,9,10]
# 3 번방을 원함 -> 3 번방은 이미 찬 상태 -> 현재 빈방 확인 (3 번방 보다 큰 비어있는 방) -> 5 번방 배정 - 현재 빈방 [6,7,8,9,10]
# 1 번방을 원함 -> 1 번방은 이미 찬 상태 -> 현재 빈방 확인 (1 번방 보다 큰 비어있는 방) -> 6 번방 배정 - 현재 빈방 [7,8,9,10]
