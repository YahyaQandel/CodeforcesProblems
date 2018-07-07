stringOne = input()
stringTwo = input()

if stringOne.lower() < stringTwo.lower():
    print(-1)
elif stringOne.lower() > stringTwo.lower():
    print(1)
else:
    print(0)