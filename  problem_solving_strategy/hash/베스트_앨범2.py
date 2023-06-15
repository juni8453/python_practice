from collections import defaultdict

def solution(genres, plays):
    answer = []

    # {0: ['classic', 500], 1: ['pop', 600], 2: ['classic', 150], 3: ['classic', 800], 4: ['pop', 2500]})
    song_index = defaultdict(list)
    for i in range(len(genres)):
        song_index[i] = [genres[i], plays[i]]

    print(song_index)

    # {'classic': 1450, 'pop': 3100})
    play_sum = defaultdict(int)
    for i in range(len(genres)):
        play_sum[genres[i]] += plays[i]

    # 1. 장르별 총 재생 횟수를 기준으로 내림차순으로 정렬된 장르 리스트 생성
    # play_sum 의 key 가 기준이니 x 는 key 값, 즉 key 값 기준 내림차순
    # ['pop', 'classic']
    sorted_genres = sorted(play_sum, key=lambda x: play_sum[x], reverse=True)

    for genre in sorted_genres:
        # 2. 장르별로 (재생 횟수, 고유 번호)의 튜플을 리스트로 저장하고, 재생 횟수에 따라 인덱스 (노래번호) 내림차순으로 정렬
        genre_songs = sorted([song for song in song_index.items() if song[1][0] == genre],
                             key=lambda x: x[1][1], reverse=True)

        # 3. 각 장르에서 가장 많이 재생된 노래 두 개의 인덱스를 선택하여 answer에 추가
        # append 를 사용하면 [[4, 1], [3, 0]] 으로 저장되니까 추출해서 저장하기 위해 extend() 사용
        answer.extend([song[0] for song in genre_songs[:2]])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
