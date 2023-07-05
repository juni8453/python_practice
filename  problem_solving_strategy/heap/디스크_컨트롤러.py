from heapq import heappush, heappop


def solution(jobs):
    # 작업 요청부터 종료까지 걸린 시간 answer
    # 현재 시간 now
    # 처리한 일의 개수 i
    # 이전 작업 시작 완료 시간 start
    answer, now, i, start = 0, 0, 0, -1
    heap = []

    while i < len(jobs):
        for job in jobs:
            # 요청 시간이 이전 작업의 시작시간보다 크고, 현재 시간보다 작거나 같은 작업을 최소 힙에 삽입
            if start < job[0] <= now:
                heappush(heap, [job[1], job[0]])

        # 처리할 작업이 있는 경우라면
        if len(heap) > 0:
            cur = heappop(heap)
            start = now             # 시작 시간을 현재 시간으로 갱신
            now += cur[0]           # 현재 시간에서 작업 소요 시간을 더해 현재 시간을 갱신
            answer += now - cur[1]  # 대기 시간 및 처리 시간 누석
            i += 1                  # 일을 하나 처리했으므로 처리한 일의 개수 증가


        # 처리할 작업이 없는 경우라면
        else:
            now += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))