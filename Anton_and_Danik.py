x = input()
matches = input()
anton = 0
danik = 0
for i in matches:
    if i=='A':
        anton = anton+1
    else:
        danik = danik+1

if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print('Friendship')