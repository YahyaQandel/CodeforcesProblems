s = input()
t = input()

s_count = 0
steps = 1

for i in t:
    if s[s_count] == i:
        steps+=1
        s_count += 1

print(steps)