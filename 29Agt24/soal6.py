nb = float(input("Masukkan total belanja: "))

p_terendah = 25
sisa = nb % p_terendah
nb_bulat = nb - sisa

print(f'Nilai belanja setelah di bulatkan : Rp.{nb_bulat} ')