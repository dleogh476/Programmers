def solution(s):
    answer = ''
    list = s.split(' ')

    list_int = [int(a) for a in list]

    #list_of_integers = [int(x) for x in list]

    listOfmax = max(list_int)
    listOfmin = min(list_int)
    #print(listOfmax.type())
    #anwer를 list로 착각
    #answer.insert(0, listOfmax)
    #answer.insert(2, listOfmin)
    
    #answer = listOfmin + ' ' + listOfmax
    answer = "%d %d" %(listOfmin, listOfmax)
    return answer

