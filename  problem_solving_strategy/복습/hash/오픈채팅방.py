def solution(records):
    logs = []
    answer = []
    record_dict = dict()

    for record in records:
        split = record.split()
        sign = split[0]
        uid = split[1]
        nickname = ''

        if sign != 'Leave':
            nickname = split[2]

        # 채팅방에 접속한 유저 딕셔너리에 저장
        # uid 를 파악해서 nickname 으로 교체하기 위해 uid 님이 들어왔습니다. 형식으로 저장
        if sign == 'Enter':
            record_dict[uid] = nickname
            logs.append(uid + ',' + '님이 들어왔습니다.')

        # uid 를 파악해서 nickname 으로 교체하기 위해 uid 님이 나갔습니다. 형식으로 저장
        if sign == 'Leave':
            logs.append(uid + ',' + '님이 나갔습니다.')

        # 바뀐 닉네임이 있다면 uid key 에 매칭되는 nickname vlaue 갱신
        if sign == 'Change':
            record_dict[uid] = nickname

    # answer 에 저장된 uid 를 현 상태의 nickname 으로 교체하면 끝.
    for log in logs:
        split = log.split(',')
        uid = split[0]

        answer.append(log.replace(uid, record_dict[uid]).replace(',', ''))

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# return ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]