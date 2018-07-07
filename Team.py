problems = input()
count_trust = 0
implemented_problems = 0

for i in range(0,int(problems)):
    trust_line = input()
    trust_line = trust_line.split(' ')
    for j in trust_line:
        if j=='1':
            count_trust+=1

    if count_trust >1:
        implemented_problems +=1
    count_trust = 0

print(implemented_problems)