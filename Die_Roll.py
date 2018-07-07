y_w = list(map(int, input().rstrip().split()))
prob_1 = max(y_w[0],y_w[1])
prob_2 = 7 - prob_1

if prob_2 == 1:
    print('1/6')

if prob_2 == 2:
    print('1/3')

if prob_2 == 3:
    print('1/2')

if prob_2 == 4:
    print('2/3')

if prob_2 == 5:
    print('5/6')

if prob_2 == 6:
    print('1/1')