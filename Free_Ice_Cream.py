n_x = input().split(" ")
n = int(n_x[0])
x = int(n_x[1])
distressed_kids = 0
total = x
for i in range(n):
    input_packs = input().split(" ")
    packs = int(input_packs[1])
    packs_type = input_packs[0]
    if packs_type == "+":
        total += packs
    else:
        if total < packs:
            distressed_kids += 1
        else:
            total -= packs

print("{} {}".format(total, distressed_kids))
