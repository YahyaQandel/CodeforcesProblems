cols = 1
rows = 0
for i in range(1,6):
    c = input()
    row = c.split(' ')
    row = list(map(int, row))
    if 1 in row:
        cols = row.index(1) + 1
        rows = i
rows_trials = abs(rows-3)
cols_trials = abs(cols-3)
print(rows_trials+cols_trials)