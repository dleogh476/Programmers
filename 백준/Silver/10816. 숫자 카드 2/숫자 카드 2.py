from collections import Counter
answer = []
N_count = input()
N = input()
M_count = input()
M = input()

N_list = N.split(' ')
M_list = M.split(' ')

N_type = Counter(N_list)

for m_element in M_list:
    if m_element in N_type:
        answer.append(N_type[m_element])
    else:
        answer.append(0)

#print(answer)
for num in answer:
    print(num, end=' ')