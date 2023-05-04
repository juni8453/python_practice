# 항상 재귀 return 을 주의하자. 비워도 되는지, 다음 스택에 차있는 재귀 부분에서 사용해야하는지 잘 판단해야한다.
# 실수한다면 'NoneType' and 'int' 등의 예외를 만나게 됨.

def find_empty_room(want, rooms):
    if want not in rooms:
        rooms[want] = want + 1
        return want

    empty = find_empty_room(rooms[want], rooms)
    rooms[want] = empty + 1
    return empty


def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        find_empty_room(num, rooms)

    return list(rooms)


print(solution(10, [1,3,4,1,3,1]))