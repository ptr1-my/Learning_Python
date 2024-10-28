n = input("Masukkan Nama Anda: aqw")
gp = int(input("Masukkan Nominal Gaji Pokok Anda: "))

t = int(0.20*gp)
p = int((0.15*gp)+t)
gb = int(gp+t-p)

print(f"Nama Karyawan : {n} Gaji Bersih : {gb}")