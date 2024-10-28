x = int(input("Jarak tempuh semut dalam satuan cm : "))



km = int(x/100000)
sisa = x%100000
m = int (sisa/1000)
cm = sisa%1000

print(f'X = {x} cm, ini berarti semut menempuh jarak sejauh\n{km} "km +" {m} "m +"" {cm} "cm"')