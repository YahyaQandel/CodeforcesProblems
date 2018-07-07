username = input()
s = "".join(set(username))
if len(s)%2 == 0: print("CHAT WITH HER!")
else: print("IGNORE HIM!")