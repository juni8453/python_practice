
def solution(bandage, health, attacks):
    a_dict = dict()

    for time, damage in attacks:
        a_dict[time] = damage

    cur_time = 1
    continue_s = 0
    max_health = health

    while len(a_dict) != 0:
        if cur_time in a_dict and a_dict[cur_time] != 0: # 현재 시간에 몬스터 공격이 있는 경우,           
            continue_s = 0 # 연속 성공횟수 초기화
            health -= a_dict[cur_time] # 공격력만큼 체력 저하
            del a_dict[cur_time] # 몬스터 공격 후 딕셔너리에서 삭제

            if health <= 0: # 사망
                return -1

        else: # 현재 시간에 몬스터 공격이 없는 경우,
            continue_s += 1  # 연속 성공 횟수 추가

            if continue_s == bandage[0]:
                health += bandage[1] + bandage[2] # 추가 체력만큼 더 회복
                continue_s = 0 # 추가 체력만큼 회복했으니 다시 초기화

            else:
                health += bandage[1]

            if health > max_health: # 회복 후 최대 체력을 넘는다면 최대 체력으로 초기화
                health = max_health

        cur_time += 1

    return health

# 지금 time 에 몬스터 공격이 없는 경우,
# 계속해서 붕대 감기 시전
# 만약 연속으로 붕대감기에 성공한다면 추가 회복량만큼 더해서 체력 회복