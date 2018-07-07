word = input()

upperCounter=0
lowerCounter=0
for char in word:
    if char.islower():
        lowerCounter+=1
    else:
        upperCounter+=1

if lowerCounter >= upperCounter:
    print(word.lower())
elif lowerCounter < upperCounter:
    print(word.upper())