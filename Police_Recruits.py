cases_number = input()
cases = list(map(int, input().rstrip().split()))
untreated_cases = 0
free_police_officer = False
hired_police_officers = 0

for i in cases:
    # print('i: '+str(i)+' ,PO: '+str(hired_police_officers)+', UN: '+str(untreated_cases))
    if i == -1 and hired_police_officers > 0:
        hired_police_officers -= 1
    elif i == -1 and hired_police_officers == 0 :
        untreated_cases += 1
    else:
        hired_police_officers += i


print(untreated_cases)