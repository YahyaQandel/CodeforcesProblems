horse_shoes = list(map(int, input().rstrip().split()))
number_of_new_shoes = 0

first = horse_shoes[0]
second = horse_shoes[1]
third = horse_shoes[2]
fourth = horse_shoes[3]

del horse_shoes[0]

if first in horse_shoes:
    number_of_new_shoes+=1

del horse_shoes[0]

if second in horse_shoes:
    number_of_new_shoes+=1

del horse_shoes[0]

if third in horse_shoes:
    number_of_new_shoes+=1



print(number_of_new_shoes)