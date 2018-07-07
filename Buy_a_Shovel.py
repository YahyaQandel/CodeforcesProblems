input_arr = list(map(int, input().rstrip().split()))
shovel_price = input_arr[0]
r = input_arr[1]

rest_change = shovel_price%10
min_shovels = 0
for i in range(1,10):
    if (i*rest_change)%r == 0 or (i*rest_change)%10 == r or (i*rest_change)%10 == 0:
        if i*shovel_price % 10 == r:
            min_shovels = i
            break
        elif i*shovel_price % 10 ==0:
            min_shovels = i
            break;




print(min_shovels)