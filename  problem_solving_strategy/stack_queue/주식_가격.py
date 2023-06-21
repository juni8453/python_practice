from collections import deque

# 첫 풀이 O(n^2)
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        sec = 0
        p = prices.popleft()

        for price in prices:
            sec += 1
            if price < p:
                break

        answer.append(sec)

    return answer

print(solution(prices=[1, 2, 3, 2, 3]))