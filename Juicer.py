conditions = list(map(int, input().rstrip().split()))
number_of_oranges = conditions[0]
max_orange_size = conditions[1]
waste_section_max_size = conditions[2]
oranges = list(map(int, input().rstrip().split()))

waste_section_clear_times = 0
total_oranges_sum = 0
for i in oranges:
    if i > max_orange_size:continue
    total_oranges_sum+=i
    if total_oranges_sum > waste_section_max_size:
        waste_section_clear_times+=1
        total_oranges_sum = 0

print(waste_section_clear_times)