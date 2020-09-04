numbers = list(map(int,input().split('+')))
res = ""
numbers.sort()
for i in range(len(numbers)):
    if i:
        res+="+"
    res+=str(numbers[i])

print(res)