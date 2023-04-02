def lru(cacheSize, cache ,city_name):
    add_time = 5
    cache_len =len(cache)
    
    #cache 아무것도 없으면 miss
    if cache_len == 0:
        cache.append(city_name)
        return add_time
    #print(cache)
    for idx in range(cache_len):
        #hit
        city_cache_low = cache[idx].lower()
        city_name_low = city_name.lower()
        if city_cache_low == city_name_low:
            del cache[idx]
            cache.append(city_name)
            add_time = 1
            return add_time
    
    #if문 실행 못하고 나오면 miss 
    add_time = 5
     
    if cache_len >= cacheSize:
        cache.pop(0)
        cache.append(city_name)   
    else:
        cache.append(city_name)
        
    return add_time


def solution(cacheSize, cities):
    answer = 0
    cache = list()
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    for idx , city in enumerate(cities):
        answer += lru(cacheSize,cache, city)
    #print(cache)       
    return answer


    