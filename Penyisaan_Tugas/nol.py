# menetukkan bilangan bulat, positif, negatif, nol

a = float(int(input("Masukkan Bilangan : ")))

def cek_bilangan(a):
    if a > 0:
        return "Positif"
    elif a < 0:
        return "Negatif"
    
def cek_tipe(a):
    return "Bulat" if a == int(a) else "Desimal"

print(f'{a} adalah {cek_tipe(a)} dan {cek_bilangan(a)}')