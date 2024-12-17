r = int(input("Masukkan jari-jari : "))
s = int(input("Masukkan s : "))
t = int(input("Masukkan t : "))

Phi = 3.14
r2 = r*r
selimut = Phi*r*s
permukaan = (Phi*r*s)+(Phi*r2)
volume = 1/3*Phi*r2*t

print(f'Luas Selimut Kerucut Adalah : {round(selimut,2)}\nLuas Permukaan Kerucut : {round(permukaan,2)}\nVolume Kerucut : {round(volume,2)}')