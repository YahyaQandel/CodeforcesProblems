cols = input()
row = []
numberOfCubesPerCol = input()
cubesList = numberOfCubesPerCol.split(' ')
cubesList = list(map(int, cubesList))

cubesList.sort(key=int)
cubesString = ""
counter=0
for i in cubesList:
    cubesString+=str(i)
    counter+=1
    if counter < len(cubesList):
        cubesString+=" "

print(cubesString)