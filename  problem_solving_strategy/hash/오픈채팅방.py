def solution(records):
    answer = []
    records_dict = dict()

    for record in records:
        split = record.split()
        keyword = split[0] # Enter, Leave, Change
        uid = split[1] # uid1234 ..
        nickname = '' # Muzi ..

        if keyword != 'Leave':
            nickname = split[2]

        if keyword == 'Enter':
            records_dict[uid] = nickname
            answer.append(uid + '님이 들어왔습니다.')

        if keyword == 'Leave':
            answer.append(uid + '님이 나갔습니다.')

        if keyword == 'Change':
            records_dict[uid] = nickname

    for i in range(len(answer)):
        uid, action = answer[i].split('님')
        change_nickname = records_dict[uid]
        answer[i] = change_nickname + '님' + action

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))