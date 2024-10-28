# alas x tinggi : 2

print ("="*25)
print ("PROGRAM SEGITIGA")
print ("="*25)

a = float(input("Masukkan Alas : "))
t = float(input("Masukkan Tinggi : "))
c = float(input("Masukkan Sisi Miring : "))

r1 = (a*t)/2
r2 = a+t+c

print(f'Luas : {round(r1,2)} cm2')
print(f'Kelilng : {round(r2,2)} cm')