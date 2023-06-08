# 내 풀이
# 장르 우선순위 깔끔하게 표현하는 법?
- 참고풀이1 과 비교 할 때, d는 dic, total_play는 genreSort 로 똑같이 데이터를 정리해두고 값을 정렬로 뽑았는데, 코드는 참고풀이1이 훨씬 간결해보인다.
- 풀이1에서는 d를 먼저 정의해두고, 이를 이용해서 genreSort를 한 줄에 바로 구했기 때문이다.
def solution(genres, plays):
    answer = []

    total_play = {}
    for i, x in enumerate(genres):
        total_play[x] = total_play.get(x, 0) + plays[i]
    total_play = sorted(total_play.items(), key=lambda x: -x[1])
    total_play = [x[0] for x in total_play]

    dic = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
        dic[genre] = dic.get(genre, []) + [(play, i)]


    for genre in total_play:
        answer += [x[1] for x in sorted(dic[genre], key=lambda x: (-x[0], x[1]))[:2]]
    return answer

# 참고풀이 1
- d = {e:[] for e in set(genres)} 이렇게 딕셔너리도 리스트처럼 초기화 할 수 있구나.
- temp[:min(len(temp), 2)] 이렇게 표현할 수 있었구나.
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

# 참고풀이 2
- 파이썬 class에서 self이런 거랑 같이 나오는 풀이들을 이해를 못한다. 이 부분을 배워 두자.
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play