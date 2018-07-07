x = input()
limak = int(x.split(' ')[0])
bob = int(x.split(' ')[1])

years=0
while limak <= bob :
    years+=1
    limak *= 3
    bob *=2
    
print(years)