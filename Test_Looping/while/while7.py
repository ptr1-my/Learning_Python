# 4. 2 + 4 + 6 + 8 + 10 = 30
i = 2
total = 0
output = ""
while i <= 10:
    output += str(i)
    total += i
    i += 2
    if i <= 10:
        output += " + "
print(f"{output} = {total}")