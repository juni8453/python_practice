from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 1. 각 장르별 총 재생횟수를 저장
    # {'classic': 1450, 'pop': 3100}
    play_count = dict()
    for i in range(len(genres)):
        play_count[genres[i]] = play_count.get(genres[i], 0) + plays[i]

    # 1-1. 총 재생 횟수의 Key 값으로 Value 를 추출하고, 해당 Value 기준 내림차순 정렬
    # ['pop', 'classic']
    sorted_genres = sorted(play_count, key=lambda x: play_count[x], reverse=True)

    # 2. Key 값이 해당 노래의 번호, Value 값이 [장르, 해당 노래의 재생횟수]
    # {0: ['classic', 500], 1: ['pop', 600], 2: ['classic', 150], 3: ['classic', 800], 4: ['pop', 2500]})
    song_index = defaultdict(list)
    for i in range(len(genres)):
        song_index[i] = [genres[i], plays[i]]

    # 가장 총 재생횟수가 많은 장르부터 탐색
    # [(4, ['pop', 2500]), (1, ['pop', 600])]
    # [(3, ['classic', 800]), (0, ['classic', 500]), (2, ['classic', 150])]
    for genre in sorted_genres:
        genre_songs = sorted([song for song in song_index.items() if song[1][0] == genre],
                             key=lambda x: (x[1][1], x[1]), reverse=True)

        answer.extend([song[0] for song in genre_songs[:2]])

    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))