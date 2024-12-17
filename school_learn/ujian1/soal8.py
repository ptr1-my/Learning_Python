print("="*25)
print("PROGRAM GEOGMETRI TABUNG")
print("="*25)

r = float(input("Masukkan Jari-jari : "))
t = float(input("Masukkan Tinggi : "))

r2 = r*r
Phi = 3.14
v = 2*Phi*r*t
l = (Phi*r2)+(Phi*r*t)

print (f"Volume Tabung : {round(v,2)}\nLuas Permukaan Tabung : {round(l,2)}")