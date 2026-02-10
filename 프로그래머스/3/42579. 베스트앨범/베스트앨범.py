def solution(genres, plays):
    answer = []
    genre_total = {}
    genre_songs = {}
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        genre_total[g] = genre_total.get(g, 0) + p
        
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((p, i))
        
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    for g, total in sorted_genres:
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        
        for s in songs[:2]:
            answer.append(s[1])
        
    return answer