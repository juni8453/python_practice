n = int(input())
house_spots = list(map(int, input().split()))

# 항상 중앙에 안테나를 설치해야 각 집까지의 거리 차이 합이 최소가 된다.
house_spots.sort()
print(house_spots[(n - 1) // 2])

