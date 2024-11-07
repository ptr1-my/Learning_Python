suhu = int(input("Masukkan Derajat Zat : "))

if suhu <= 0:
    print("Zat Adalah es")
if suhu <= 100 and suhu >= 1:
    print("Zat Adalah air")
if suhu >= 100:
    print("Zat Adalah uap")