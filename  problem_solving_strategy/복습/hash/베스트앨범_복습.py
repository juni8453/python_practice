from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_count = dict()

    for i in range(len(genres)):
        play_count[genres[i]] = play_count.get(genres[i], 0) + plays[i]


    # 각 장르별 총 재생 횟수 내림차순
    # sorted_genres = sorted(play_count, key=lambda x: play_count[x], reverse=True)
    sorted_genres = sorted(play_count, key=lambda x: x[1], reverse=True)

    song_index = defaultdict(list)
    for i in range(len(genres)):
        song_index[i] = [genres[i], plays[i]]

    for genre in sorted_genres:
        # 각 장르별 곡 리스트를 뽑아낸다.
        # [(1, ['pop', 600]), (4, ['pop', 2500])]
        # [(0, ['classic', 500]), (2, ['classic', 150]), (3, ['classic', 800])]
        cur_genres = [cur_genre for cur_genre in song_index.items() if cur_genre[1][0] == genre]

        # 재생 순서대로 내림차순 정렬
        cur_genres = sorted(cur_genres, key=lambda x: x[1][1], reverse=True)
        answer.extend(index[0] for index in cur_genres[:2])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))