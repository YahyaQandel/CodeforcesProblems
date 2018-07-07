s = input()
n = int (s.split(' ')[0])
h = int (s.split(' ')[1])
width = 0
w = input()
for i in  w.split(' '):
    if int(i) > h:
        width+=2
    else:
        width+=1

print(width)