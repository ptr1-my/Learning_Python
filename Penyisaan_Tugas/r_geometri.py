a = int(input("Masukkan Suku Pertama: "))
r = int(input("Masukkan Rasio: "))
n = int(input("Masukkan Suku ke-n: "))


def jsuku_n (a, r, n):
    if r == 1:
        return a*n
    else:
        return a*(r**n-1) / (r-1)
    
jumlah = jsuku_n (a, r, n)
print (f'Jumlah {n} Suku pertama adalah {jumlah}')