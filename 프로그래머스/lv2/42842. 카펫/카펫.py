def solution(brown, yellow):
    answer = []
    x = (brown + 4 + ((brown + 4)**2 - 16*(brown + yellow))**0.5)//4
    y = (brown + yellow)//x
    print(x,y)
    answer = x, y
    return answer