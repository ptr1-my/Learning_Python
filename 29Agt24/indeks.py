# indeks nilai mahasiswa

n = int(input('Masukkan nilai ujian : '))

if n >= 80:
    print(f"Nilai Ujian = {n} Indeks nilai = A")
elif n >= 70 < 80:
    print(f"Nilai Ujian = {n} Indeks nilai = B")
elif n >= 55 < 70:
    print(f"Nilai Ujian = {n} Indeks nilai = C")
elif n >= 40 < 55:
    print(f"Nilai Ujian = {n} Indeks nilai = D")
elif n < 40:
    print(f"Nilai Ujian = {n} indeks nilai = E")