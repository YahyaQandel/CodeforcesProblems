cals_index = list(map(int, input().rstrip().split()))
seconds = list(map(int, input()))
cals_sum = 0
for i in seconds:
    cals_sum += cals_index[i-1]
print(cals_sum)
