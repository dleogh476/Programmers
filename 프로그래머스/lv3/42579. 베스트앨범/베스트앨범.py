from collections import defaultdict as ddict
from pprint import pprint as pp

def solution(genres, plays):
    answer = []
    genres_inf = ddict(list)
    genres_sort = dict()
        
    # 1. key: 장르 value: [고유번호, 노래재생횟수]
    for index in range(len(genres)):
        genres_inf[genres[index]].append([index, plays[index]])
        
    # 2. 장르별 플레이 횟수 기준으로 정렬
    for inf in genres_inf:
        genres_sort[inf] = 0
        for i in genres_inf[inf]:
            genres_sort[inf] += i[1]
            
    genres_sort = sorted(genres_sort.items(),
                         key = lambda x:x[1], reverse=True)
    
    # 3. 노래 수록
    for name in genres_sort:        
        print(name)
        
        genres_inf[name[0]] = sorted(genres_inf[name[0]], 
                                 key = lambda x : x[1], reverse=True)
        
        answer.append(genres_inf[name[0]][0][0])
        if len(genres_inf[name[0]]) > 1: 
            answer.append(genres_inf[name[0]][1][0])
        
    
    # 4. 결과 확인         
    pp(genres_inf)
    
    return answer