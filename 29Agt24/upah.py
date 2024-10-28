n = input("Masukkan Nama Anda : ")
g = input('Masukkan Golongan Pekerjaan Anda : ').lower()
j = int(input('Masukkan Seluruh Jam Kerja Anda 1 Minggu Kebelakang : '))

A = 4000
B = 5000
C = 6000
D = 7500

if j <= 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {A*j}')
elif j <= 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {B*j}')
elif j <= 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {C*j}')
elif j <= 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {D*j}')

l = j - 48

if j > 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {(A*j)+(l*A)}\n dari upah mingguan {A*j} dan upah lembur {l*A}')
elif j > 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {(B*j)+(l*B)}\n dari upah mingguan {B*j} dan upah lembur {l*B}')
elif j > 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {(C*j)+(l*C)}\n dari upah mingguan {C*j} dan upah lembur {l*C}')
elif j > 48:
    print(f'Karyawan {n} mendapatkan upah sebesar {(D*j)+(l*D)}\n dari upah mingguan {D*j} dan upah lembur {l*D}')