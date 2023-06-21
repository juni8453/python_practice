def solution(progresses, speeds):
    answer = []
    times = []

    for i in range(len(progresses)):
        tmp = (100 - progresses[i]) % speeds[i]
        if tmp == 0:
            times.append((100 - progresses[i]) // speeds[i])
        else:
            times.append((100 - progresses[i]) // speeds[i] + 1)

    stack = [times[0]]
    for i in range(1, len(times)):
        big = max(stack)
        if big >= times[i]:
            stack.append(times[i])

        elif big < times[i]:
            size = len(stack)
            answer.append(size)
            stack.clear()

            stack.append(times[i])

    if len(stack) != 0:
        answer.append(len(stack))

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
